from chat2_sdk import Chat2Printer
import imageio
import cv2
from PIL import Image
import threading
import os

cap = cv2.VideoCapture('ba.flv')
cam = cv2.VideoCapture(0)
sz = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
      int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fps = 24
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
writer = imageio.get_writer('result.mp4', 'ffmpeg', fps=fps)
printer = Chat2Printer()


def do_print():
    im = Image.open('frame.jpg')
    printer.print_image(image=im)


while cap.isOpened():
    ret, frame = cap.read()
    ret2, frame2 = cam.read()
    cv2.imshow('image', frame)
    k = cv2.waitKey(20)
    # q键退出，p键打印
    if k & 0xff == ord('/90'):
        im = Image.fromarray(frame)
        im.save('frame.jpg')
        threading.Thread(target=do_print).start()
        # os.system('python do_print.py')
    if k & 0xff == ord('q'):
        break
    writer.append_data(frame2)

writer.close()
cap.release()
cam.release()
cv2.destroyAllWindows()