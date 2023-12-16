from gpiozero import Device, OutputDevice # Consider using a specific device class instead?
from gpiozero.tools import booleanized, all_values

# Pin Definitons:
pulse_pin_num = 4 # Board pin 7

# set up GPIO
pulse_pin = OutputDevice(pulse_pin_num)

print ('setting PUL- : HIGH')

# disable stepper
pulse_pin.on()
