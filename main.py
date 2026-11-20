import cv2

videoStream = cv2.VideoCapture("TrafficAtSignal.mp4")

if not videoStream.isOpened():
    print("Error reading video")
    exit()

while True:
    ret, frame = videoStream.read()
    if not ret:
        break;

    cv2.imshow("Video Player", frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

videoStream.release()
cv2.destroyAllWindows()

