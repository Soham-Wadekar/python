import cv2

img = cv2.imread("computer_vision/resources/images/cat.jpg")
print(img)

cv2.imshow("Cat", img)

cv2.waitKey(0)
