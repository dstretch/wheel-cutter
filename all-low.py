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

# disable stepper
GPIO.output(enablePin, GPIO.LOW)

# set direction pin LOW
GPIO.output(directionPin, GPIO.LOW)

# set pulse pin low
GPIO.output(pulsePin, GPIO.LOW)

print ('setting all pins low: ENA-, DIR- and PUL-')
