import os
from time import sleep
import random

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarning(False)
GPIO.setup(16, GPIO.IN)

while (GPIO.input(16) == False):
  print("Continue")
else:
  print("Pausing music")
