import cv2
import numpy as np
import sys

imgPath = 'data/picture.jpg'
img_BGR = cv2.imread(imgPath)

if img_BGR is None:
    print('Image Load Fail!')
    sys.exit()

imgResize = cv2.resize(img_BGR, (1280, 720))

print(img_BGR.shape)

cv2.imshow('lenna', img_BGR)
cv2.imshow('resize', imgResize)
key = cv2.waitKey(0)
cv2.destroyWindow('lenna')