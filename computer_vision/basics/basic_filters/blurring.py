import cv2

img = cv2.imread("computer_vision/resources/images/cat.jpg")
cv2.imshow("Original", img)

def blur(image, ksize=3, technique="gaussian"):
    match technique:
        case "gaussian": return cv2.GaussianBlur(image, (ksize, ksize), sigmaX=cv2.BORDER_DEFAULT)
        case "average": return cv2.blur(image, (ksize, ksize))
        case "box": return cv2.blur(image, (ksize, ksize))
        case "median": return cv2.medianBlur(image, ksize)
        case _: raise ValueError("Incorrect blurring technique!")

gaussian_blur = blur(img, ksize=5)
avg_blur = blur(img, ksize=3, technique='average')
median_blur = blur(img, ksize=7, technique='median')

cv2.imshow("Gaussian Blur", gaussian_blur)
cv2.imshow("Average / Box Blur", avg_blur)
cv2.imshow("Median Blur", median_blur)

cv2.waitKey(0)