import cv2
from cvzone.HandTrackingModule import HandDetector

# Parameters
width, height = 1280, 720

# Webcam
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# Hand Detector
detector = HandDetector(maxHands=2, detectionCon=0.8)

while cv2.waitKey(1) != ord('q'):
    # Get the frame from the webcam
    ret, img = capture.read()

    # Hands
    hands, img = detector.findHands(img)

    data = []
    # Landmark values - (x, y, z) * 21
    if hands:
        # Get the first hand detected
        hand = hands[0]
        # Get the landmark list
        lmList = hand['lmList']
        print(lmList)
        for lm in lmList:
            data.extend([lm[0], height - lm[1], lm[3]])

    # Draw result
    cv2.imshow("VideoFrame", img)


capture.release()
cv2.destroyAllWindows()