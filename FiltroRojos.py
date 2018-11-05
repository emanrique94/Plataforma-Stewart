import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    

    #HSV hue set value
    valorBajoRojo = np.array([150, 150, 150])
    valorAltoRojo = np.array([180, 255, 255])
    mask = cv2.inRange(hsv, valorBajoRojo, valorAltoRojo)
    res = cv2.bitwise_and(frame, frame, mask = mask)
    
    cv2.imshow("Camara", frame)
    cv2.imshow("Umbral", mask)
    cv2.imshow("Resta", res)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release()        

