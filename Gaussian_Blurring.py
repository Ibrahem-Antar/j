import cv2 as cv

img = cv.imread("Task 1 Pic.png")
cv.imshow('Before', img)

# Convert to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Grayscale", gray)

gaussianBlurImg = cv.GaussianBlur(img, (3,3) , 0)

cv.imshow("After",gaussianBlurImg)
cv.waitKey(0)