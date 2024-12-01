import cv2
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8")

# Paint the image a certain color
blank[200:300, 300:400] = 0, 255, 0

# Draw a rectangle
cv2.rectangle(blank, (0, 0), (300, 400), color=(255, 0, 0), thickness=5)

# Draw a circle
cv2.circle(
    blank, (250, 250), 150, color=(0, 0, 255), thickness=2
)  # Thickness = -1 for filled

# Draw a line
cv2.line(blank, (150, 250), (300, 500), color=(255, 255, 255), thickness=4)

# Write text on an image
cv2.putText(
    blank,
    "Text",
    org=(100, 200),
    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
    fontScale=2,
    color=(0, 255, 255),
    thickness=2,
)

cv2.imshow("Image", blank)
cv2.waitKey(0)
