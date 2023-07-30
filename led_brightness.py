from serial import Serial
import cvzone
import math
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np

serialcomm = Serial('COM4', 9600) 
serialcomm.timeout = 1
cap=cv2.VideoCapture(0) 
detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    success, img = cap.read()
    img = cv2.resize(img, (640,480))
    hand, img = detector.findHands(img, flipType=True)
    
    if hand:
        lmList = hand[0]['lmList']
        
        x1,y1 = lmList[4][0:2]
        x2,y2 = lmList[8][0:2]
        
        cv2.circle(img, (x1,y1), 7, (0,255,255),1)
        cv2.circle(img, (x2,y2), 7, (0,255,255),1)
        
        cv2.line(img, (x1,y1), (x2,y2),(0,255,0),2)
        # to calculate the distance between two finger tips
        d=int(math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) * 1.0))
              
        d1 = np.interp(d, [0, 200], [0, 100])
        
        e='\n'
                
        if 0 <= d1 < 256:
            serialcomm.write(str(d).encode())
            serialcomm.write(e.encode())
    cv2.imshow('Image',img)  
    if (cv2.waitKey(1) & 0xff == ord('q')): 
        cap.release()
        serialcomm.close()
        break

cv2.destroyAllWindows()