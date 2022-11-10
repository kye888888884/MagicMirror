import mediapipe as mp
import cv2
import time
import numpy as np
import pandas as pd
import os
mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils # For drawing keypoints
points = mpPose.PoseLandmark # 33 Landmarks
path = "DATASET/TRAIN/plank" # enter dataset path
data = [] # 132 Landmark Data with x, y, z and vis
for p in points:
        x = str(p)[13:]
        data.append(x + "_x")
        data.append(x + "_y")
        data.append(x + "_z")
        data.append(x + "_vis")

data = pd.DataFrame(columns = data) # Empty dataset

# Display my cam
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while cv2.waitKey(33) != ord('q'):
    # Get my original cam
    ret, img = capture.read()

    # Recognize blaze pose of my cam
    temp = []
    blackie = np.zeros(img.shape)
    results = pose.process(img)

    if results.pose_landmarks:
        # Add landmarks to my cam display
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS) #draw landmarks on image

        landmarks = results.pose_landmarks.landmark

        for i,j in zip(points,landmarks):
            temp = temp + [j.x, j.y, j.z, j.visibility]

    # Draw result
    cv2.imshow("VideoFrame", img)


capture.release()
cv2.destroyAllWindows()