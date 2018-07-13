#Wheel Cutter Application
#version 1.0
#Written by Mark Baird
#
#requires the following modules to be installed as follows:
# pip3 install guizero


from guizero import App, Text,TextBox, PushButton, Window, yesno
import RPi.GPIO as GPIO
import time

# Pin Definitons:
enablePin = 2
directionPin = 3
pulsePin = 4

#Global variables
teethToCut = 60
stepsPerRev = 8000
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
    GPIO.output(pulsePin, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(pulsePin, GPIO.LOW)
    time.sleep(delay)


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
  GPIO.output(enablePin, GPIO.HIGH)

def closeCutting():
  global currentTooth

  reallySure = yesno("Question", "Do you really want to finish cutting?")
  #only close if sure!
  if reallySure == True:
    cuttingWindow.hide()
    currentTooth = 1
    lblCurrentTooth.value = currentTooth
    GPIO.output(enablePin, GPIO.LOW)


#App code starts running here!

# setup gpio
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(enablePin, GPIO.OUT)
GPIO.setup(directionPin, GPIO.OUT)
GPIO.setup(pulsePin, GPIO.OUT)

# disable stepper
GPIO.output(enablePin, GPIO.LOW)

# set direction
GPIO.output(directionPin, GPIO.HIGH)

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
cuttingWindow = Window(app, title="Cutting teeth", width=200, height=100, layout="grid")
cuttingWindow.hide()
cuttingWindow.on_close(closeCutting)
app.focus()
lblCurrentTooth = Text(cuttingWindow, size=16, text="1", grid=[0,0])
lblOf = Text(cuttingWindow, size=16, text="of", grid=[1,0])
lblTotalTeeth = Text(cuttingWindow, size=16, text="", grid=[2,0])
lblTotalTeeth.value = teethToCut
#btnBack = PushButton(cuttingWindow, text="Back", grid=[0,1])
btnNext = PushButton(cuttingWindow, command=nextTooth, text="Next", grid=[1,1])
#btnFinish = PushButton(cuttingWindow, text="Finish", grid=[2,1])
app.display()
