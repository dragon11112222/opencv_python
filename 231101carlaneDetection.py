import cv2

filePath = 'data/solidWhiteCurve.jpg'
img = cv2.imread(filePath)
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray = cv2.imread(filePath, cv2.IMREAD_GRAYSCALE)

cv2.imshow('result', img)
cv2.imshow('result2', img_gray)


cv2.waitKey(0)
cv2.destroyAllWindows()