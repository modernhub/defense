import cv2


def take_photo():
    cap = cv2.VideoCapture(0)
    for i in range(30):
        cap.read()

    ret, frame = cap.read()
    cv2.imwrite('./image/cam.png', frame)
    cap.release()

