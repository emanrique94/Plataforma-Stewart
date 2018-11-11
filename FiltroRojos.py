import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    _,frame = cap.read()
    #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # lower mask (0-10)
    lower_red = np.array([0,50,50])
    upper_red = np.array([10,255,255])
    mask0 = cv2.inRange(img_hsv, lower_red, upper_red)
    # upper mask (170-180)
    lower_red = np.array([125, 150, 50])
    upper_red = np.array([180, 255, 255])
    #lower_red = np.array([170,50,50])
    #upper_red = np.array([180,255,255])
    mask1 = cv2.inRange(img_hsv, lower_red, upper_red)
    # join my masks
    mask = mask0+mask1
    # set my output img to zero everywhere except my mask
    output_img = frame.copy()
    output_img[np.where(mask==0)] = 0
    # or your HSV image, which I *believe* is what you want
    output_hsv = img_hsv.copy()
    output_hsv[np.where(mask==0)] = 0
    # res matrix comparar
    res = cv2.bitwise_and(frame, frame, mask = mask)
    #output_hsv =  cv2.imshow("hsv", output_hsv)
    #mask = cv2.imshow("mask", mask)    
    frame  =  cv2.imshow("Camara", frame)
    res = cv2.imshow("res", res)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release()        