import cv2
import mediapipe as mp
from cvzone.HandTrackingModule import HandDetector

#cap=cv2.VideoCapture(0)

detector = HandDetector(detectionCon=0.8, maxHands=2)

#while True:
img=cv2.imread("test4.jpg")
img=cv2.resize(img, (400,400))
#flags=cv2.IMREAD_COLOR
hands, img=detector.findHands(img)
#no draw -> hands = =detector.findHands(img, draw=False)

if hands:
    #hand 1
    hand1 = hands[0]
    lmList1=hand1["lmList"] #list of landmark points
    bbox1=hand1["bbox"] #bounding box info x,y,w,h
    centerPoint1=hand1["center"] #center of hand cx, cy
    handType1=hand1["type"] #left or right
    fingers1=detector.fingersUp(hand1)
    print(lmList1)
    print(bbox1)

cv2.imshow("Image", img)
cv2.waitKey(0)
