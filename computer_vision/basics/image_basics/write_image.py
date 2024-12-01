import cv2
import numpy as np

noise = np.random.rand(500, 500)
cv2.imshow("", noise)

cv2.imwrite("computer_vision/resources/images/noisy.jpg", noise)
cv2.waitKey(0)
