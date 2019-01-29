import cv2

cam = cv2.VideoCapture(0)

while cam.isOpened():
    ret, frame = cam.read()
    cv2.imshow('camera', frame)
    k = cv2.waitKey(20)
    if k & 0xff == ord('q'):
        break