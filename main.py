import cv2

SHOW_STREAM = True

cap = cv2.VideoCapture(0)
while True:
    ret, image = cap.read()

    if SHOW_STREAM:
        cv2.imshow('stream', image)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()
