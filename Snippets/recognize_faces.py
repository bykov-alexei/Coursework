import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import face_recognition

threshold = 0.6

actors_files = os.listdir('actors')
actors_encodings = {}
for filename in actors_files:
    actor_name = filename.split('.')[0]
    
    img = plt.imread(os.path.join('actors', filename))[:, :, :3].astype('uint8')
    print(filename)
    encoding = face_recognition.face_encodings(img)[0]
    actors_encodings[actor_name] = encoding

img = plt.imread('friends.jpg')[:, :, :3].astype('uint8')
locations = face_recognition.face_locations(img)
encodings = face_recognition.face_encodings(img)
for location, encoding in zip(locations, encodings):  
    confidencies = {actor: np.linalg.norm(actor_encoding - encoding) for actor, actor_encoding in actors_encodings.items()} 
    actor, confidence = min(confidencies.items(), key=lambda x: x[1])
    if confidence > threshold:
        name = 'Unknown'
    else:
        name = actor

    cv2.rectangle(img, (location[1], location[0]), (location[3], location[2]), (255, 0, 0), 2)
    cv2.putText(img, name, (location[3], location[2] + 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
plt.imsave('face_recognition_result.jpg', img)