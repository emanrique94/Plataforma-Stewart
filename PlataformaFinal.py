# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685


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

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second 1M
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)
    
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

print('Moving servo on channel 0, press Ctrl-C to quit...')
while True:
    #move servos
    posicionInicial()
    time.sleep(5)
    posicionAlta12()


   
