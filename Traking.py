import cv2
import numpy as np
import time
import numpy

cap = cv2.VideoCapture(0)
width = 160
heidth = 120 

cap.set(3, width)
cap.set(4, heidth)
f = int(8)
c = int(16)
Cuadrantes=[]

while(1):
    # Take each frame
    _,frameRed = cap.read() 
    #print(cap.get(4))
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frameRed, cv2.COLOR_BGR2HSV)
    # define range of blue color in HSV
    LowerRed = np.array([125, 125, 125])
    UpperRed = np.array([180, 255, 255])
    # Threshold the HSV image to get only blue colors
    maskRed = cv2.inRange(hsv, LowerRed, UpperRed)
    # Bitwise-AND mask and original image
    resRed = cv2.bitwise_and(frameRed, frameRed, mask = maskRed)

    for x in range(f):
        Cuadrantes.append([0]*c)      
    for row in range(0, 119): #heidth-1): 160
        for col in range(0, 159): #width-1): 120
            j = int(col/10)
            i = int(row/15)
            Cuadrantes[int(i)][int(j)] += resRed[row, col, 2]
    max = -1
    maxi = 0
    maxj = 0
    for rowCuadrantes in range(0, f):
        for colCuadrantes in range(0, c):
            if Cuadrantes[rowCuadrantes][colCuadrantes] > max:
                max = Cuadrantes[rowCuadrantes][colCuadrantes]
                maxi = rowCuadrantes
                maxj = colCuadrantes
            
            
    print(maxi)
    print(maxj)            #if  Cuadrantes[0][0] > 0:
    
    #Show input            
    #frameRed  =  cv2.imshow("Camara", frameRed)
    #maskRed = cv2.imshow("mask", maskRed)
    #resRed = cv2.imshow("Res", resRed)

    #Exit camera with esc
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release()  