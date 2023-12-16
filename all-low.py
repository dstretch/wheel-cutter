from gpiozero import Device, OutputDevice # Consider using a specific device class instead?
from gpiozero.tools import booleanized, all_values

# Pin Definitons:
enable_pin_num = 2 # Board pin 3
direction_pin_num = 3 # Board pin 5
pulse_pin_num = 4 # Board pin 7

# set up GPIO
enable_pin = OutputDevice(enable_pin_num)
direction_pin = OutputDevice(direction_pin_num)
pulse_pin = OutputDevice(pulse_pin_num)

print ('setting all pins low: ENA-, DIR- and PUL-')

# disable stepper
enable_pin.off()

# set direction pin LOW
direction_pin.off()

# set pulse pin low
pulse_pin.off()
