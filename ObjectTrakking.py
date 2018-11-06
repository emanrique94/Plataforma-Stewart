import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    # Take each frame
    _, frameBlue = cap.read()
    _,frameRed = cap.read()
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frameBlue, cv2.COLOR_BGR2HSV)
    hsv = cv2.cvtColor(frameRed, cv2.COLOR_BGR2HSV)
    # define range of blue color in HSV
    LowerBlue = np.array([110,50,50])
    UpperBlue = np.array([130,255,255])
    LowerRed = np.array([125, 125, 125])
    UpperRed = np.array([180, 255, 255])
    # Threshold the HSV image to get only blue colors
    maskBlue = cv2.inRange(hsv, lower_blue, upper_blue)
    maskRed = cv2.inRange(hsv, LowerRed, UpperRed)
    # Bitwise-AND mask and original image
    resBlue = cv2.bitwise_and(frameBlue,frameRed, mask= maskBlue)
    resRed = cv2.bitwise_and(frameRed, frameRed, mask = maskRed)
    #Show input
    frameBlue = cv2.imshow('frame Blue',frameBlue)
    maskBlue = cv2.imshow('mask Blue',maskBlue)
    resBlue = cv2.imshow('res Blue',resBlue)
    frameRed  =  cv2.imshow("Camara", frameRed)
    maskRed = cv2.imshow("mask", maskRed)
    resRed = cv2.imshow("Res", resRed)

    #Exit camera with esc
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release()  