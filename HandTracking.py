import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
pTime=0
while True:
    success, img = cap.read()
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img, f'FPS:{int(fps)}', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Test", img)
    cv2.waitKey(1)

'''
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, image = cap.read()
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(imageRGB);

    #checking whether a hand is detected
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks: #working with each hand
            for id, lm in enumerate(handLms.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                if id==20:
                    cv2.circle(image, (cx, cy)m 25, (255, 0, 255), cv2.FILLED)  
            mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)
    
    #display
    cv2.imshow("Output", image)
    cv2.waitKey(1)
'''