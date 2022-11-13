import cv2
import mediapipe as mp
from sklearn.svm import SVC

# Display my cam
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Read data
data = pd.read_csv("dataset3.csv")
X,Y = data.iloc[:,:132],data['target']

# Set model
model = SVC(kernel = 'poly')
model.fit(X,Y)
mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils
path = "enter image path"
img = cv2.imread(path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
results = pose.process(imgRGB)
if results.pose_landmarks:
    landmarks = results.pose_landmarks.landmark
    for j in landmarks:
            temp = temp + [j.x, j.y, j.z, j.visibility]
    y = model.predict([temp])
    if y == 0:
        asan = "plank"
    else:
        asan = "goddess"
    print(asan)
    cv2.putText(img, asan, (50,50), cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),3)
    cv2.imshow("image",img)