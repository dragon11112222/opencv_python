import cv2
import numpy as np
import sys

imgPath = 'data/picture.jpg'
img_BGR = cv2.imread(imgPath)

if img_BGR is None:
    print('Image Load Fail!')
    sys.exit()

imgResize = cv2.resize(img_BGR, (1280, 720))
imgResize2 = cv2.resize(img_BGR, dsize = (0, 0), fx = 0.7, fy = 0.4)

print(img_BGR.shape)

cv2.imshow('lenna', img_BGR)
cv2.imshow('resize', imgResize)
cv2.imshow('resize2', imgResize2)
key = cv2.waitKey(0)
cv2.destroyWindow('lenna')