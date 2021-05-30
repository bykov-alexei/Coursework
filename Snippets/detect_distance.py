import cv2
import face_recognition

cap = cv2.VideoCapture(0)

D = 1
W = 0.1
F = None

last_location = None
while(True):
    ret, frame = cap.read()

    rgb_frame = frame[:, :, [2, 1, 0]]
    locations = face_recognition.face_locations(rgb_frame)
    if len(locations) > 0:
        last_location = locations[-1]
        print("Face detected. Place your face at 1 meter and press E")
    
    for location in locations:
        left, top, right, bottom = location
        cv2.rectangle(frame, (top, left), (bottom, right), (0, 255, 0), 3)
    
    if cv2.waitKey(1) & 0xFF == ord('e'):
        left, _, right, _ = last_location
        P = (right - left)
        F = (P * D) / W
        print('Calibrated. F is equal to ' + str(F))
        break

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()