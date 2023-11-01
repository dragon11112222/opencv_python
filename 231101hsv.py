import cv2
import sys

src = cv2.imread('data/trafficLight.png')

if src is None:
    print('Image load failed!')
    sys.exit()
