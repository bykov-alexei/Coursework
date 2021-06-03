import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import face_recognition

def get_embedding(img):
    img = img[:, :, :3].astype('uint8')
    encodings = face_recognition.face_encodings(img)
    if len(encodings) == 1:
        return encodings[0]
    else:
        return None