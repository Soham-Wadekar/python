"""Thresholding is a technique in image processing used to segment an image by converting grayscale images into binary or multi-level images."""

import cv2

img = cv2.imread("computer_vision/resources/images/louvre.jpg", 0)

_, thresh_binary = cv2.threshold(img, 125, 250, type=cv2.THRESH_BINARY)
_, thresh_binary_inv = cv2.threshold(img, 125, 250, type=cv2.THRESH_BINARY_INV)
_, thresh_trunc = cv2.threshold(img, 125, 250, type=cv2.THRESH_TRUNC)
_, thresh_tozero = cv2.threshold(img, 125, 250, type=cv2.THRESH_TOZERO)
_, thresh_tozero_inv = cv2.threshold(img, 125, 250, type=cv2.THRESH_TOZERO_INV)

cv2.imshow("Binary", thresh_binary)
cv2.imshow("Binary Inv", thresh_binary_inv)
cv2.imshow("Trunc", thresh_trunc)
cv2.imshow("ToZero", thresh_tozero)
cv2.imshow("ToZero Inv", thresh_tozero_inv)

cv2.waitKey(0)
