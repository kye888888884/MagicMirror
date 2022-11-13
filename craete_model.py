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

count = 0

for img in os.listdir(path):
    if count > 3:
        break
    temp = []
    
    img = cv2.imread(path + "/" + img)
    imageWidth, imageHeight = img.shape[:2]
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    blackie = np.zeros(img.shape) # Blank image
    results = pose.process(imgRGB)
    print("results: ", results.pose_landmarks)

    if results.pose_landmarks:

        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS) #draw landmarks on image

        # mpDraw.draw_landmarks(blackie, results.pose_landmarks, mpPose.POSE_CONNECTIONS) # draw landmarks on blackie

        landmarks = results.pose_landmarks.landmark

        for i,j in zip(points,landmarks):
            print(type(j))
            temp = temp + [j.x, j.y, j.z, j.visibility]

        data.loc[count] = temp

        count +=1

    cv2.imshow("Image", img)

    cv2.imshow("blackie",blackie)

    cv2.waitKey(100)

data.to_csv("dataset3.csv") # save the data as a csv file