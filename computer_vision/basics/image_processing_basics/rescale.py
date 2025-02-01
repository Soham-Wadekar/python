import cv2

img = cv2.imread("computer_vision/resources/images/louvre.jpg")


def rescale(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)


cv2.imshow("Before rescaling", img)
img_rescaled = rescale(img, 0.5)
cv2.imshow("After rescaling", img_rescaled)

cv2.waitKey(0)
