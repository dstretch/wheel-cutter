from gpiozero import Device, OutputDevice # Consider using a specific device class instead?
from gpiozero.tools import booleanized, all_values

# Pin Definitons:
direction_pin_num = 3 # Board pin 5

# set up GPIO
direction_pin = OutputDevice(direction_pin_num)

print ('setting DIR- : HIGH')

# disable stepper
direction_pin.on()
