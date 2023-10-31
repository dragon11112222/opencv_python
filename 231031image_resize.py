import cv2
import numpy as np

imgPath = 'data/picture.jpg'
img_BGR = cv2.imread(imgPath)

print(img_BGR.shape)