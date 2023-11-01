import cv2
import numpy as np


filePath = 'data/solidWhiteCurve.jpg'
img = cv2.imread(filePath)

# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray = cv2.imread(filePath, cv2.IMREAD_GRAYSCALE)

img_gray_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)

low_thrshld = 50
high_thrshld = 400
img_gray_blur_canny = cv2.Canny(img_gray_blur, low_thrshld, high_thrshld)

mask = np.zeros_like(img)
print(img.shape)  ## left top 기준 (height, width, filter)
point1 = (100, img.shape[0])
point2 = (450, 320)
point3 = (550, 320)
point4 = (img.shape[1] - 20, img.shape[0])
vertices = np.array([[point1, point2, point3, point4]], dtype=np.int32)
mask_color = (255, 255, 255)
cv2.fillPoly(mask, vertices, mask_color)

cv2.imshow('result', img)
cv2.imshow('result2', img_gray)
cv2.imshow('result3', img_gray_blur)
cv2.imshow('result4', img_gray_blur_canny)
cv2.imshow('result5', mask)


cv2.waitKey(0)
cv2.destroyAllWindows()