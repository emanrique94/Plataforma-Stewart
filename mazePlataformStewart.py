from __future__ import division
import cv2
import numpy as np
import time
import numpy
# Import the PCA9685 module.
import Adafruit_PCA9685
#board object
pwm = Adafruit_PCA9685.PCA9685()
# Inicializar camara y parametros de tamaño
cap = cv2.VideoCapture(0)
width = 320
heidth = 240
cap.set(3, width)
cap.set(4, heidth)
# linea color para marcar cuadrantes camara 
line = 150

#Pareja 0 y 5

PulsoAlto5 = 1200
PulsoMedio5 = 1500
PulsoBajo5 = 1800

PulsoAlto0 = 1800
PulsoMedio0 = 1500
PulsoBajo0 = 1200

#Pareja 1 y 2

PulsoAlto1= 1200
PulsoMedio1 = 1500
PulsoBajo1 = 1800

PulsoAlto2 = 1800
PulsoMedio2 = 1500
PulsoBajo2 = 1200

#Pareja 3 y 4 

PulsoAlto4 = 1800
PulsoMedio4 = 1500
PulsoBajo4 = 1200

PulsoAlto3 = 1200
PulsoMedio3 = 1500
PulsoBajo3 = 1800
#cuenta
count = 0


def posicionInicial():
    #parejas 0 y 5
    pulso0normalchanel0 = int(PulsoMedio0 / (1000000/60) * 4095)
    pulso0normalchanel5 = int(PulsoMedio5 / (1000000/60) * 4095)
    
    # parejas  1 y 2
    pulso0normalchanel1 = int(PulsoMedio1 / (1000000/60) * 4095)
    pulso0normalchanel2 = int(PulsoMedio2 / (1000000/60) * 4095)
    
    # parejas 3 y 4
    pulso0normalchanel3 = int(PulsoMedio3 / (1000000/60) * 4095)
    pulso0normalchanel4 = int(PulsoMedio4 / (1000000/60) * 4095)
    
    #Motion
    pwm.set_pwm(1, 0, pulso0normalchanel1)
    time.sleep(0.5)
    pwm.set_pwm(2, 0, pulso0normalchanel2)
    time.sleep(0.5)
    pwm.set_pwm(4, 0, pulso0normalchanel4)
    time.sleep(0.5)
    pwm.set_pwm(3, 0, pulso0normalchanel3)
    time.sleep(0.5)
    pwm.set_pwm(5, 0, pulso0normalchanel5)
    time.sleep(0.5)
    pwm.set_pwm(0, 0, pulso0normalchanel0)
    time.sleep(0.5)


while(1):
    #iniciar motores
    posicionInicial()
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
    _,frame = cap.read() 
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
            Cuadrantes[int(i)][int(j)] += mask[row, col]
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
    # Mostrar resultados
    #output_hsv =  cv2.imshow("hsv", output_hsv)
    #mask = cv2.imshow("mask", mask)    
    #frame  =  cv2.imshow("Camara", frame)
    res = cv2.imshow("res", res)
    # cerrar con esc
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release()