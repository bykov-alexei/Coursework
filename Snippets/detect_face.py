import face_recognition
import matplotlib.pyplot as plt
import cv2

image = face_recognition.load_image_file('friends.jpg')
face_locations = face_recognition.face_locations(image)
for location in face_locations:
    cv2.rectangle(image, (location[1], location[0]), (location[3], location[2]), (255, 0, 0), 2)
plt.imsave('face_detection_result.jpg', image)