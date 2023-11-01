import cv2

filePath = 'data/solidWhiteCurve.jpg'
img = cv2.imread(filePath)
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray = cv2.imread(filePath, cv2.IMREAD_GRAYSCALE)
img_gray_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)
low_thrshld = 50
high_thrshld = 200
img_gray_blur_canny = cv2.Canny(img_gray_blur, low_thrshld, high_thrshld)

cv2.imshow('result', img)
cv2.imshow('result2', img_gray)
cv2.imshow('result3', img_gray_blur)
cv2.imshow('result4', img_gray_blur_canny)


cv2.waitKey(0)
cv2.destroyAllWindows()