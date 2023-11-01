import cv2

img = cv2.imread('data/solidWhiteCurve.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('result', img)
cv2.imshow('result2', img_gray)


cv2.waitKey(0)
cv2.destroyAllWindows()