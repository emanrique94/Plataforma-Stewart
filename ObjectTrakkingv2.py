import cv2
import numpy as np
import time
import numpy

cap = cv2.VideoCapture(0)
width = 160
heidth = 120 

cap.set(3, width)
cap.set(4, heidth)

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
    #Show input
    #print(resRed.shape)
    #print(resRed[0,0, 2])
    f= int(8)
    #print(f)
    c = int(16)
    Cuadrantes=[]
    for x in range(f):
        Cuadrantes.append([0]*c)
        
    #print(numpy.shape(C uadrantes))
    #print('')
    
    for row in range(0, 119): #heidth-1): 160
        for col in range(0, 159): #width-1): 120
            j = int(col/10)
            i = int(row/15)
            #print(j)

#print(i)
            #print("inicio")
            #zzz = Cuadrantes[j][i]
            #print(zzz)
            #print(numpy.shape(Cuadrantes))
            
            Cuadrantes[int(i)][int(j)] += resRed[row, col, 2]
            #print(Cuadrantes[int(j)][int(i)])
            
            #print(Cuadrantes[int(j)][int(i)])
            
            
            
            
            
            
            
            
            
            
            
            
            
            if resRed[row, col, 2] != 0:
                #print([row, col, 2])
                #print (resRed[row, col, 2])
                print()
            if col == width/2:
                resRed[row, col, 1]= 255
            if col == 1/16*width:
                resRed[row, col, 2]= 180
            if col == 2/16*width:
                resRed[row, col, 2]= 180
            if col == 3/16*width:
                resRed[row, col, 2]= 180
            if col == 4/16*width:
                resRed[row, col, 2]= 180
            if col == 5/16*width:
                resRed[row, col, 2]= 180
            if col == 6/16*width:
                resRed[row, col, 2]= 180
            if col == 7/16*width:
                resRed[row, col, 2]= 180
            if col == 8/16*width:
                resRed[row, col, 2]= 180
            if col == 9/16*width:
                resRed[row, col, 2]= 180
            if col == 10/16*width:
                resRed[row, col, 2]= 180
            if col == 11/16*width:
                resRed[row, col, 2]= 180
            if col == 12/16*width:
                resRed[row, col, 2]= 180
            if col == 13/16*width:
                resRed[row, col, 2]= 180
            if col == 14/16*width:
                resRed[row, col, 2]= 180
            if col == 15/16*width:
                resRed[row, col, 2]= 180
            if col == width:
                resRed[row, col, 2]= 180
            if row == heidth/2:
                resRed[row, col, 1]= 255
            if row == 1/16*heidth:
                resRed[row, col, 2]= 180
            if row == 2/16*heidth:
                resRed[row, col, 2]= 180
            if row == 3/16*heidth:
                resRed[row, col, 2]= 180
            if row == 4/16*heidth:
                resRed[row, col, 2]= 180
            if row == 5/16*heidth:
                resRed[row, col, 2]= 180
            if row == 6/16*heidth:
                resRed[row, col, 2]= 180
            if row == 7/16*heidth:
                resRed[row, col, 2]= 180
            if row == 8/16*heidth:
                resRed[row, col, 2]= 180
            if row == 9/16*heidth:
                resRed[row, col, 2]= 180
            if row == 10/16*heidth:
                resRed[row, col, 2]= 180
            if row == 11/16*heidth:
                resRed[row, col, 2]= 180
            if row == 12/16*heidth:
                resRed[row, col, 2]= 180
            if row == 13/16*heidth:
                resRed[row, col, 2]= 180
            if row == 14/16*heidth:
                resRed[row, col, 2]= 180
            if row == 15/16*heidth:
                resRed[row, col, 2]= 180
            if row == 16/16*heidth:
                resRed[row, col, 2]= 180
                
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
            #print("es mayor")
    
                
            

                
    #time.sleep(5)
    #frameRed  =  cv2.imshow("Camara", frameRed)
    #maskRed = cv2.imshow("mask", maskRed)
    #resRed = cv2.imshow("Res", resRed)

    #Exit camera with esc
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release()  