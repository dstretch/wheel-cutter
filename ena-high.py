from gpiozero import Device, OutputDevice # Consider using a specific device class instead?
from gpiozero.tools import booleanized, all_values

# Pin Definitons:
enable_pin_num = 2 # Board pin 3

# set up GPIO
enable_pin = OutputDevice(enable_pin_num)

print ('setting ENA- : HIGH')

# disable stepper
enable_pin.on()
