import cv2
import sys

cap = cv2.VideoCapture('data/woman.mp4')

if not cap.isOpened():
    print('video open failed!')
    sys.exit()


def cartoon_filter(img):
    h, w = img.shape[:2]
    img2 = cv2.resize(img, (w//2, h//2))

    blr = cv2.bilateralFilter(img2, -1, 20, 7)
    edge = 255 - cv2.Canny(img2, 80, 120)
    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)

    dst = cv2.bitwise_and(blr, edge)
    dst = cv2.resize(dst, (w, h), interpolation=cv2.INTER_NEAREST)

    return dst



if not cap.isOpened():
    print('video open failed!')
    sys.exit()

cam_mode = 1

while True:
    ret, frame = cap.read()

    if not ret:
        break

    if cam_mode == 1:
        frame = cartoon_filter(frame)


    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)




cap.release()
cv2.destroyAllWindows()