import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
pTime = 0
mpPose = mp.solutions.pose
pose = mpPose.Pose()
# mpHands = mp.solutions.hands
# my_hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)

    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks,mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h,w,c = img.shape
            print(id, lm)
            #pixel value로 변환
            cx,cy = int(lm.x*w), int(lm.y*h)
            cv2.circle(img, (cx,cy),5,(255,0,0), cv2.FILLED)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)),(70,50), cv2.FONT_HERSHEY_PLAIN,3,(255,0,0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)