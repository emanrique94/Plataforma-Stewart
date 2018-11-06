import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    _,frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    

    #HSV hue set value
    valorBajoRojo = np.array([125, 125, 125])
    valorAltoRojo = np.array([180, 255, 255])
    mask = cv2.inRange(hsv, valorBajoRojo, valorAltoRojo)
    res = cv2.bitwise_and(frame, frame, mask = mask)
    
    frame  =  cv2.imshow("Camara", frame)
    mask = cv2.imshow("mask", mask)
    res = cv2.imshow("Res", res)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release()        