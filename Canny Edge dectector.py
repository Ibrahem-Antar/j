import cv2 as cv

# Load the image
img = cv.imread("Task 2 pic.png")
cv.imshow('Before', img)

# Convert to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Grayscale", gray)

canny = cv.Canny(img, 50, 175)

cv.imshow('After', canny)
cv.waitKey(0)