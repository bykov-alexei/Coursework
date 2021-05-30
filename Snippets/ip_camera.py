import cv2
import face_recognition

cap = cv2.VideoCapture('rtsp://alexei:alexei@192.168.1.5:8080/h264_ulaw.sdp')

D = 1
W = 0.1
F = None

last_location = None
while True:
    ret, frame = cap.read()
    print(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()