import cv2
import numpy as np
import sys

imgPath = 'data/picture.jpg'
img_BGR = cv2.imread(imgPath)

if img_BGR is None:
    print('Image Load Fail!')
    sys.exit()

print(img_BGR.shape)