import cv2
import sys

filePath = 'data/trafficLight.png'
src = cv2.imread(filePath)

if src is None:
    print('Image load failed!')
    sys.exit()

src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)