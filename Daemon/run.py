import time
import datetime
from camera import Camera, DetectorAPI

detection_model = DetectorAPI('faster_rcnn_inception_v2_coco_2018_01_28/frozen_inference_graph.pb')


while True:
    start = time.time()
    cameras = Camera.get_all()
    # print(cameras)
    for camera in cameras:
        camera.process(detection_model)
    end = time.time()
    if (end - start) < 1:
        time.sleep(1 - (end - start))
    print('Processed', datetime.datetime.now())