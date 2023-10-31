import cv2
import sys

imgPath = 'data/cannyTest.png'
imgBGR = cv2.imread(imgPath)

if imgBGR is None:
    print('Load is Fail!')
    sys.exit()