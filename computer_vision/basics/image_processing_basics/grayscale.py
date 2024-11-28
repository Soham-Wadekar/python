import cv2

img = cv2.imread("computer_vision/resources/images/cat.jpg")
cv2.imshow("Original", img)

grayscale_img = cv2.cvtColor(img, code=cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", grayscale_img)

cv2.waitKey(0)