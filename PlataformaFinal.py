# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time
import cv2
import numpy as np
import  matplotlib
from PIL import Image

# Import the PCA9685 module.
import Adafruit_PCA9685
# inicializar camara 
cap = cv2.VideoCapture(0)


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
#servo_min = 150  # Min pulse length out of 4096
#servo_max = 600  # Max pulse length out of 4096

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
    #motion
    
    pwm.set_pwm(1, 0, pulso0normalchanel1)
    time.sleep(1)
    pwm.set_pwm(2, 0, pulso0normalchanel2)
    time.sleep(1)
    pwm.set_pwm(4, 0, pulso0normalchanel4)
    time.sleep(1)
    pwm.set_pwm(3, 0, pulso0normalchanel3)
    time.sleep(1)
    pwm.set_pwm(5, 0, pulso0normalchanel5)
    time.sleep(1)
    pwm.set_pwm(0, 0, pulso0normalchanel0)
    time.sleep(1)
    
def posicionAlta12():
    #parejas 0 y 5
    pulso0normalchanel0 = int(PulsoBajo0 / (1000000/60) * 4095)
    pulso0normalchanel5 = int(PulsoBajo5 / (1000000/60) * 4095)
    
    # parejas  1 y 2
    pulso0normalchanel1 = int(PulsoAlto1 / (1000000/60) * 4095)
    pulso0normalchanel2 = int(PulsoAlto2 / (1000000/60) * 4095)
    
    # parejas 3 y 4
    pulso0normalchanel3 = int(PulsoBajo3 / (1000000/60) * 4095)
    pulso0normalchanel4 = int(PulsoBajo4 / (1000000/60) * 4095)
    #motion

    pwm.set_pwm(1, 0, pulso0normalchanel1)
    time.sleep(2)
    pwm.set_pwm(2, 0, pulso0normalchanel2)
    time.sleep(2)
    pwm.set_pwm(3, 0, pulso0normalchanel3)
    time.sleep(2)
    pwm.set_pwm(4, 0, pulso0normalchanel4)
    time.sleep(2)
    pwm.set_pwm(0, 0, pulso0normalchanel0)
    time.sleep(2)
    pwm.set_pwm(5, 0, pulso0normalchanel5)
    time.sleep(2)
    
def posicionAlta05():
    #parejas 0 y 5
    pulso0normalchanel0 = int(PulsoAlto0 / (1000000/60) * 4095)
    pulso0normalchanel5 = int(PulsoAlto5 / (1000000/60) * 4095)
    
    # parejas  1 y 2
    pulso0normalchanel1 = int(PulsoBajo1 / (1000000/60) * 4095)
    pulso0normalchanel2 = int(PulsoBajo2 / (1000000/60) * 4095)
    
    # parejas 3 y 4
    pulso0normalchanel3 = int(PulsoAlto3 / (1000000/60) * 4095)
    pulso0normalchanel4 = int(PulsoAlto4 / (1000000/60) * 4095)
    #motion
    pwm.set_pwm(5, 0, pulso0normalchanel5)
    time.sleep(2)
    pwm.set_pwm(0, 0, pulso0normalchanel0)
    time.sleep(2)
    pwm.set_pwm(2, 0, pulso0normalchanel2)
    time.sleep(2)
    pwm.set_pwm(1, 0, pulso0normalchanel1)
    time.sleep(2)
    pwm.set_pwm(4, 0, pulso0normalchanel4)
    time.sleep(2)
    pwm.set_pwm(3, 0, pulso0normalchanel3)
    time.sleep(2)
    
def posicionAlta34():
    #parejas 0 y 5
    pulso0normalchanel0 = int(PulsoBajo0 / (1000000/60) * 4095)
    pulso0normalchanel5 = int(PulsoBajo5 / (1000000/60) * 4095)
    
    # parejas  1 y 2
    pulso0normalchanel1 = int(PulsoBajo1 / (1000000/60) * 4095)
    pulso0normalchanel2 = int(PulsoBajo2 / (1000000/60) * 4095)
    
    # parejas 3 y 4
    pulso0normalchanel3 = int(PulsoAlto3 / (1000000/60) * 4095)
    pulso0normalchanel4 = int(PulsoAlto4 / (1000000/60) * 4095)
    #motion
    pwm.set_pwm(5, 0, pulso0normalchanel5)
    time.sleep(2)
    pwm.set_pwm(0, 0, pulso0normalchanel0)
    time.sleep(2)
    pwm.set_pwm(2, 0, pulso0normalchanel2)
    time.sleep(2)
    pwm.set_pwm(1, 0, pulso0normalchanel1)
    time.sleep(2)
    pwm.set_pwm(4, 0, pulso0normalchanel4)
    time.sleep(2)
    pwm.set_pwm(3, 0, pulso0normalchanel3)
    time.sleep(2)
    
# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

def detect(image):
    bitmap = cv2.fromarray(image)
    
print('Moving servo on channel 0, press Ctrl-C to quit...')
while(1):
    # Take each frame
    _,frameRed = cap.read()
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
    frameRed  =  cv2.imshow("red", frameRed)
    #maskBlue = cv2.imshow('mask Blue',maskBlue)
    resRed = cv2.imshow("Res", resRed)
    #save photho
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    #cv2.imwrite("frame%d.jpg" % count, cap) 
    #Exit camera with esc
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    
cv2.destroyAllWindows()
cap.release() 