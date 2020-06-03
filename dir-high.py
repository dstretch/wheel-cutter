import RPi.GPIO as GPIO
import time

# Pin Definitons:
enablePin = 2
directionPin = 3
pulsePin = 4

# setup gpio
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(enablePin, GPIO.OUT)
GPIO.setup(directionPin, GPIO.OUT)
GPIO.setup(pulsePin, GPIO.OUT)

# set direction pin HIGH
GPIO.output(directionPin, GPIO.HIGH)

print ('setting DIR- : HIGH')
