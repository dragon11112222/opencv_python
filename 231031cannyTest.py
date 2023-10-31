import cv2
import sys

imgPath = 'data/cannyTest.png'
imgBGR = cv2.imread(imgPath)
imgGray = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)

if imgBGR is None:
    print('Load is Fail!')
    sys.exit()

cv2.imshow('org', imgGray)
cv2.waitKey()
cv2.destroyAllWindows()