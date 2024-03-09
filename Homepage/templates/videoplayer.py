import cv2
cap = cv2.VideoCapture("video.mp4")
ret, frame = cap.read()
while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q') or not ret:
        break
cap.release()
cv2.destroyAllWindows()
