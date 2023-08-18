import cv2
import mediapipe as mp
from cvzone.HandTrackingModule import HandDetector

#cap=cv2.VideoCapture(0)

detector = HandDetector(detectionCon=0.8, maxHands=2)

#while True:
# img=cv2.imread("TrainingData/P/p19.png", flags=cv2.IMREAD_COLOR)
img=cv2.imread("SamplePic6.jpg")
# img=cv2.resize(img, (400,400))
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
    tipDist=[]
    palmDist=[]
    for i in range (1,5):
        length, info, img = detector.findDistance(lmList1[4*i][0:2],lmList1[4*i+4][0:2], img)
        tipDist.append(length)
        length, info, img = detector.findDistance(lmList1[4*i][0:2],lmList1[0][0:2], img)
        palmDist.append(length)

    length, info, img = detector.findDistance(lmList1[20][0:2],lmList1[0][0:2], img)
    palmDist.append(length)
    knuckleDist = []
    for i in range (1,6):
        for j in range (4*i-3,4*i):
            print(str(j)+" "+str(j+1))
            length, info, img = detector.findDistance(lmList1[j][0:2],lmList1[j+1][0:2], img)
            knuckleDist.append(length)
    print(fingers1)
    print("A "+str(lmList1)+str(bbox1[3]/bbox1[2])+str(palmDist)+str(tipDist)+str(knuckleDist))

    # f = open("Data.txt", "a")
    # f.write("Y "+str(lmList1)+str(bbox1[3]/bbox1[2])+str(palmDist)+str(tipDist)+str(knuckleDist)+"\n")
    # f.close()

    for i in range(21):
        if(i>0 and i<5):
            cv2.circle(img, (lmList1[i][0], lmList1[i][1]), 3, (255, 0, 0), cv2.FILLED)
        elif(i>4 and i<9):
            cv2.circle(img, (lmList1[i][0], lmList1[i][1]), 3, (0, 255, 0), cv2.FILLED)
        elif(i>8 and i<13):
            cv2.circle(img, (lmList1[i][0], lmList1[i][1]), 3, (0, 0, 0), cv2.FILLED)
        elif(i>12 and i<17):
            cv2.circle(img, (lmList1[i][0], lmList1[i][1]), 3, (0, 255, 255), cv2.FILLED)
        elif(i>16 and i<21):
            cv2.circle(img, (lmList1[i][0], lmList1[i][1]), 3, (20, 100, 50), cv2.FILLED)
# else:
#     f = open("Data.txt", "a")
#     f.write("no hand\n")
#     f.close()
cv2.imshow("Image", img)
cv2.waitKey(0)
