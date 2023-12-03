#Wheel Cutter Application
#version 1.0
#Written by Mark Baird
#
# Version 1.1
# Switched to GPIO Zero to enable running on Pi 5 
# By David Stretch
#
# GPIO Zero and guizero are pre-installed on Raspberry Pi OS Desktop images
# Other OS images might need to install them manually:
#
# sudo apt install python3-gpiozero
# pip3 install guizero (pre-installed on Raspberry Pi OS Desktop)

from guizero import App, Text,TextBox, PushButton, Window, yesno
from gpiozero import Device, OutputDevice # Consider using a specific device class instead?
from gpiozero.tools import booleanized, all_values
import time

# Pin Definitons:
enable_pin_num = 3 # Board pin 2
direction_pin_num = 5 # Board pin 3
pulse_pin_num = 7 # Board pin 4

#Global variables
teethToCut = 60
stepsPerRev = 12000
steps = []
currentTooth = 1

# reduce teeth to cut by 10
def minus10teeth():
  global teethToCut
  if teethToCut > 10:
    teethToCut = teethToCut - 10
  lblTeethCut.value = teethToCut

# reduce teeth to cut by 1
def minus1tooth():
  global teethToCut
  if teethToCut > 1:
    teethToCut = teethToCut - 1
  lblTeethCut.value = teethToCut

# increase teeth to cut by 1
def plus1tooth():
  global teethToCut
  teethToCut = teethToCut + 1
  lblTeethCut.value = teethToCut

# increase teeth to cut by 10
def plus10teeth():
  global teethToCut
  teethToCut = teethToCut + 10
  lblTeethCut.value = teethToCut


# pulse stepper by n pulses
def moveStepper(pulses):
  print("move stepper by " + str(pulses))
  delay = 0.01
  for x in range(pulses):
    pulse_pin.on()
    time.sleep(delay)
    
    pulse_pin.off()
    time.sleep(delay)
    
    #accelerate motor until max delay is 0.005
    if delay > 0.001 : delay = delay - 0.0005


# advance to next tooth
def nextTooth():
  global currentTooth
  print("next tooth " + str(currentTooth) + " steps = " + str(steps[currentTooth-1]))
  moveStepper(steps[currentTooth-1])
  currentTooth = currentTooth + 1
  if currentTooth > teethToCut: currentTooth = 1
  lblCurrentTooth.value = currentTooth

# Calculates steps for each tooth
def calculateSteps():
  global steps
  print ("calcuating steps")
  cuttingWindow.show(wait=True)
  lblTotalTeeth.value = teethToCut
  steps.clear()
  minSteps = int(stepsPerRev / teethToCut)
  division = float(stepsPerRev) / teethToCut
  stepsSoFar = 0

  for x in range(teethToCut):
    #calculate where we should be
    actual = (x+1) * division

    #is min steps enough?
    diff = actual - (stepsSoFar + minSteps)

    if diff >= 1:
      currentSteps = minSteps + 1
    else:
      currentSteps = minSteps

    #add the steps to the array
    steps.append(currentSteps)

    #keep tally of steps so far
    stepsSoFar = stepsSoFar + currentSteps
    #print("tooth " + str(x) + " then " + str(actual) + " current " + str(currentSteps)+ " total " + str(stepsSoFar) + " diff " + str(diff))
  print (steps)

  #enable the stepper ready ready for advancing
  enable_pin.on()

def closeCutting():
  global currentTooth

  reallySure = yesno("Question", "Do you really want to finish cutting?")
  #only close if sure!
  if reallySure == True:
    cuttingWindow.hide()
    currentTooth = 1
    lblCurrentTooth.value = currentTooth
    
    enable_pin.off()
    direction_pin.off()
    pulse_pin.off()
    Device.pin_factory.close()


#App code starts running here!

# set up GPIO
enable_pin = OutputDevice(enable_pin_num)
direction_pin = OutputDevice(direction_pin_num)
pulse_pin = OutputDevice(pulse_pin_num)

# disable stepper
enable_pin.off()

# set direction
direction_pin.on()

app = App(title="Wheel cutting", width=300, height=100, layout="grid")

#showing teeth to cut
lblTeeth = Text(app, size=16, text="Teeth:", grid=[0,1])
lblTeethCut = Text(app, size=16, text="60", grid=[1,1])

#buttons to adjust number of teeth
btnMinus10 = PushButton(app, command=minus10teeth, text="-10", grid=[2,1])
btnMinus1 = PushButton(app, command=minus1tooth, text="-1", grid=[3,1])
btnPlus1 = PushButton(app, command=plus1tooth, text="+1", grid=[4,1])
btnPlus10 = PushButton(app, command=plus10teeth, text="+10", grid=[5,1])

#button to start cutting
btnGo = PushButton(app, command=calculateSteps, text="Go", grid=[3,2])

#cutting window
cuttingWindow = Window(app, title="Dividing", width=200, height=100, layout="grid")
cuttingWindow.hide()
cuttingWindow.when_closed = closeCutting

app.focus()

lblCurrentTooth = Text(cuttingWindow, size=16, text="1", grid=[0,0])
lblOf = Text(cuttingWindow, size=16, text="of", grid=[1,0])
lblTotalTeeth = Text(cuttingWindow, size=16, text="", grid=[2,0])
lblTotalTeeth.value = teethToCut
#btnBack = PushButton(cuttingWindow, text="Back", grid=[0,1])
btnNext = PushButton(cuttingWindow, command=nextTooth, text="Next", grid=[1,1])
#btnFinish = PushButton(cuttingWindow, text="Finish", grid=[2,1])
app.display()
