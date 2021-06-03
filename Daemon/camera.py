import os
import pymysql
import numpy as np
import tensorflow.compat.v1 as tf
import matplotlib.pyplot as plt
import cv2
import time
import face_recognition
import base64
from uuid import uuid4 as uuid
from config import config

def connect():
    connection = pymysql.connections.Connection(**config['database'])
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    return connection, cursor


class DetectorAPI:
    def __init__(self, path_to_ckpt):
        self.path_to_ckpt = path_to_ckpt

        self.detection_graph = tf.Graph()
        with self.detection_graph.as_default():
            od_graph_def = tf.GraphDef()
            with tf.gfile.GFile(self.path_to_ckpt, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')

        self.default_graph = self.detection_graph.as_default()
        self.sess = tf.Session(graph=self.detection_graph)
        self.image_tensor = self.detection_graph.get_tensor_by_name('image_tensor:0')
        self.detection_boxes = self.detection_graph.get_tensor_by_name('detection_boxes:0')
        self.detection_scores = self.detection_graph.get_tensor_by_name('detection_scores:0')
        self.detection_classes = self.detection_graph.get_tensor_by_name('detection_classes:0')
        self.num_detections = self.detection_graph.get_tensor_by_name('num_detections:0')

    def processFrame(self, image):
        image_np_expanded = np.expand_dims(image, axis=0)
        start_time = time.time()
        (boxes, scores, classes, num) = self.sess.run(
            [self.detection_boxes, self.detection_scores, self.detection_classes, self.num_detections],
            feed_dict={self.image_tensor: image_np_expanded})
        end_time = time.time()

        # print("Elapsed Time:", end_time-start_time)

        im_height, im_width,_ = image.shape
        boxes_list = [None for i in range(boxes.shape[1])]
        for i in range(boxes.shape[1]):
            boxes_list[i] = (int(boxes[0,i,0] * im_height),
                        int(boxes[0,i,1]*im_width),
                        int(boxes[0,i,2] * im_height),
                        int(boxes[0,i,3]*im_width))

        return boxes_list, scores[0].tolist(), [int(x) for x in classes[0].tolist()], int(num[0])

    def close(self):
        self.sess.close()
        self.default_graph.close()


def find_person(embedding):
    conn, cursor = connect()
    formula = " + ".join([f"({'e%i' % i} - {embedding[i-1]}) * ({'e%i' % i} - {embedding[i-1]})" for i in range(1, 129)])
    query = f"SELECT id, name, {formula} as `proximity` FROM known_persons ORDER BY `proximity` ASC"
    cursor.execute(query)
    result = cursor.fetchone()
    if result['proximity'] < 0.6:
        return result


class Camera:

    def __init__(self, id, title, x, y, rstp, F=None, current_frame=None):
        self.id = id
        self.title = title
        self.x = x 
        self.y = y
        self.rstp = rstp
        self.F = F

        self.capture_ = cv2.VideoCapture(self.rstp)

    @staticmethod
    def get_all():
        conn, cursor = connect()
        query = "SELECT * FROM cameras"
        cursor.execute(query)
        data = cursor.fetchall()
        cameras = []
        for row in data:
            cameras.append(Camera(**row))
        conn.close()
        return cameras

    def connect(self):
        capture = cv2.VideoCapture(self.rstp)
        self.capture_ = capture

    def process(self, detection_model):
        ret, img = self.capture_.read()

        threshold = 0.7
        W = 0.1
        boxes, scores, classes, num = detection_model.processFrame(img)
        for i in range(len(boxes)):
            if classes[i] == 1 and scores[i] > threshold:
                box = boxes[i]
                human_id = str(uuid())
                human = img[box[0]:box[2], box[1]:box[3]]
                location = None
                encoding = None
                face = None
                face_id = None
                D = None
                face_locations = face_recognition.face_locations(human)
                if len(face_locations) > 0:
                    face_encodings = face_recognition.face_encodings(human)
                    if len(face_encodings) > 0:
                        location = face_locations[0]
                        encoding = face_encodings[0]
                        face = human[location[0]:location[2], location[3]:location[1]]
                        person = find_person(encoding)
                        face_id = person['id'] if person else None
                    if self.F:
                        width = abs(location[2] - location[0])
                        D = self.F * W / width

                encoding = encoding.astype('float64') if encoding is not None else None
                human_picture_filename = None
                face_picture_filename = None
                if human_id:
                    human_picture_filename = os.path.join('../images', 'humans', human_id + '.jpg')
                if face is not None:
                    face_picture_filename = os.path.join('../images', 'faces', human_id + '_face' + '.jpg')

                human_cx = (box[3] - box[1]) // 2
                human_cy = (box[2] - box[0]) // 2                

                e_string = ', '.join(["e%i" % i for i in range(1, 129)])
                if encoding is None:
                    query = "INSERT INTO occurrences"\
                            f"(human_id, face_id, camera_id, timestamp, distance, human_picture, face_picture, picture_x, picture_y)"\
                            f"VALUES (%s, %s, %s, NOW(), %s, %s, %s, %s, %s)"
                    args = (human_id, face_id, self.id, D, human_picture_filename, face_picture_filename, human_cx, human_cy,)
                else:
                    query = "INSERT INTO occurrences "\
                        f"(human_id, face_id, camera_id, timestamp, distance, human_picture, face_picture, picture_x, picture_y, {e_string}) "\
                        f"VALUES (%s, %s, %s, NOW(), %s, %s, %s, %s, %s, {', '.join(['%s' for _ in range(128)])})"
                    args = (human_id, face_id, self.id, D, human_picture_filename, face_picture_filename, human_cx, human_cy, *encoding)
                conn, cursor = connect()
                cursor.execute(query, args)

                success, a_numpy = cv2.imencode('.jpg', img)
                a = base64.b64encode(a_numpy.tobytes())

                query = "UPDATE cameras SET current_frame = %s WHERE id=%s"
                cursor.execute(query, (a, self.id))
                
                conn.commit()
                conn.close()

                if human is not None:
                    plt.imsave(human_picture_filename, human[:, :, [2, 1, 0]])
                if face is not None:
                    plt.imsave(face_picture_filename, face[:, :, [2, 1, 0]])