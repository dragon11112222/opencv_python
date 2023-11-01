import cv2
import sys
import numpy as np


filePath = 'data/solidWhiteCurve.jpg'
img = cv2.imread(filePath)

if img is None:
    print('Image load failed!')
    sys.exit()

# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray = cv2.imread(filePath, cv2.IMREAD_GRAYSCALE)

img_gray_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)

low_thrshld = 50
high_thrshld = 400
img_gray_blur_canny = cv2.Canny(img_gray_blur, low_thrshld, high_thrshld)

# 흰색 면을 걸러내려면 GaussianBlur & Canny 가지고는 안 됨! 색깔로 걸러내 줘야 함.
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def on_trackbar(pos):
    hmin = cv2.getTrackbarPos('H_min', 'dst')
    hmax = cv2.getTrackbarPos('H_max', 'dst')

    dst = cv2.inRange(img_hsv, (0, 0, hmin), (179, 20, hmax))
    cv2.imshow('dst', dst)

cv2.namedWindow('dst')
cv2.createTrackbar('H_min', 'dst', 100, 255, on_trackbar)
cv2.createTrackbar('H_max', 'dst', 255, 255, on_trackbar)
on_trackbar(0)

minRange = (0, 0, 140)
maxRange = (179, 20, 255)
img_white = cv2.inRange(img_hsv, minRange, maxRange)

mask = np.zeros_like(img_white)
print(img.shape)  ## left top 기준 (height, width, filter)
point1 = (100, img.shape[0])
point2 = (450, 320)
point3 = (550, 320)
point4 = (img.shape[1] - 20, img.shape[0])
vertices = np.array([[point1, point2, point3, point4]], dtype=np.int32)
mask_color = (255, 255, 255)
cv2.fillPoly(mask, vertices, mask_color)

print(img_white.shape)
print(mask.shape)
img_masked = cv2.bitwise_and(img_white, mask)

# img_masked를 새로운 mask 삼아 기존 이미지에서 차선만 필터링

# cv2.imshow('result', img)
# cv2.imshow('result2', img_gray)
# cv2.imshow('result3', img_gray_blur)
# cv2.imshow('result4', img_gray_blur_canny)
cv2.imshow('hsv', img_hsv)
cv2.imshow('hsv_white', img_white)
cv2.imshow('result5', mask)
cv2.imshow('result6', img_masked)

cv2.waitKey(0)
cv2.destroyAllWindows()