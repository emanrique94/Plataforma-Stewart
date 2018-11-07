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

PulsoAlto5 = 1700
PulsoMedio5 = 1500
PulsoBajo5 = 1300

PulsoAlto0 = 1700
PulsoMedio0 = 1500
PulstoBajo0 = 1300

#Pareja 1 y 2

PulsoAlto1= 1300
PulsoMedio1 = 1500
PulsoBajo1 = 1700

PulsoAlto2 = 1700
PulsoMedio2 = 1500
PulsoBajo2 = 1300

#Pareja 3 y 4 

PulsoAlto4 = 1700
PulsoMedio4 = 1500
PulsoBajo4 = 1300

PulsoAlto3 = 1700
PulsoMedio3 = 1500
PulsoBajo3 = 1300

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

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

print('Moving servo on channel 0, press Ctrl-C to quit...')
while True:
    # parejas 0 y 5
    pulso0 = 1400 # para valores menores a 1500 baja 
    pulso0normal = int(pulso0 / (1000000/60) * 4095)
    
    pulso0chanel5 = 1600 # para valores menores a 1500 baja
    pulso0normalchanel5 = int(pulso0chanel5 / (1000000/60) * 4095)

    
    # parejas 1 y 2
    pulso0chanel1 = 1700 #servo 1 para valores mayores a 1500 baja
    pulso0normalchanel1 = int(pulso0chanel1 / (1000000/60) * 4095)
    
    pulso0chanel2 = 1300 # para valores menores a 1500 baja
    pulso0normalchanel2 = int(pulso0chanel2 / (1000000/60) * 4095)
    
    # parejas 3 y 4
    pulso0chanel3 = 1700 # para valores mayores a 1500 baja
    pulso0normalchanel3 = int(pulso0chanel3 / (1000000/60) * 4095)
    
    pulso0chanel4 =  1300 # para valores menores a 1500 baja
    pulso0normalchanel4 = int(pulso0chanel4 / (1000000/60) * 4095)
    
        
    
    
# Move servo on channel O between extremes.
    pwm.set_pwm(0, 0, pulso0normal)
    time.sleep(1)
    pwm.set_pwm(1, 0, pulso0normalchanel1)
    pwm.set_pwm(2, 0, pulso0normalchanel2)
    pwm.set_pwm(3, 0, pulso0normalchanel3)
    pwm.set_pwm(4, 0, pulso0normalchanel4)
    pwm.set_pwm(5, 0, pulso0normalchanel5)
    time.sleep(1)
    #pwm.set_pwm(0, 0, 2000)
    #time.sleep(1)
