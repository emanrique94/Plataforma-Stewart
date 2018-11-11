import cv2
import numpy as np
import time
import numpy

# Inicializar camara y parametros de tamaño
cap = cv2.VideoCapture(0)
width = 320
heidth = 240
cap.set(3, width)
cap.set(4, heidth)
# linea color para marcar cuadrantes camara 
line = 150

while(1):
    # filas y colunmas 16 
    f= int(8)
    c = int(16)
    Cuadrantes=[]
    for x in range(f):
        Cuadrantes.append([0]*c)

    #NO DECLR GLOBANMENTE O LE DA LA PUTISA
    colCuadrantes = int(width/16)
    rowCuadrantes = int(heidth/8)
    # tomar un fragmento
    _,frameRed = cap.read() 
    #Cambiar de escala a hsv
    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # mascara baja de (0-10)
    lower_red = np.array([0,50,50])
    upper_red = np.array([10,255,255])
    mask0 = cv2.inRange(img_hsv, lower_red, upper_red)
    #mascara alta
    lower_red = np.array([125, 150, 50])
    upper_red = np.array([180, 255, 255])
    mask1 = cv2.inRange(img_hsv, lower_red, upper_red)
    # Concatenar mascaras
    mask = mask0+mask1
    # configuro mi salida img a cero en todas partes excepto mi máscara
    output_img = frame.copy()
    output_img[np.where(mask==0)] = 0
    # o imagen HSV, que * creo * es lo que quieres
    output_hsv = img_hsv.copy()
    output_hsv[np.where(mask==0)] = 0
    # res matrix comparar
    res = cv2.bitwise_and(frame, frame, mask = mask)
    # identificar cuadrante pelota ctual
    for row in range(0, heidth): #heidth-1): 160
        for col in range(0, width): #width-1): 120
            j = int(col/colCuadrantes)
            i = int(row/rowCuadrantes)
            Cuadrantes[int(i)][int(j)] += res[row, col, 2]
    # identeficar posicion actual        
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
    print(maxj)
    # mostrar resultados
    #output_hsv =  cv2.imshow("hsv", output_hsv)
    #mask = cv2.imshow("mask", mask)    
    frame  =  cv2.imshow("Camara", frame)
    res = cv2.imshow("res", res)
    # cerrar con esc
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release()  