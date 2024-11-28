import cv2

capture = cv2.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    cv2.imshow('Video', frame)

    if cv2.waitKey(20) and 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()