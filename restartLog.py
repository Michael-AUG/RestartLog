#!/bin/python
# Simple script for restarting the rigctl.service and log.service services at the press of a button.
# by Michael Topple GM5AUG

import RPi.GPIO as GPIO
import time
import os

# Use the Broadcom SOC Pin numbers
# Set up the Pin with internal pullups enabled and in reading mode.
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# What to do when the button is pressed
def LogRestart(channel):
    os.system("sudo systemctl restart log.service rigctld.service")

# What to execute when the button pressed event happens
GPIO.add_event_detect(18, GPIO.FALLING, callback = LogRestart, bouncetime = 2000)

#In this place I hope to add a second command which will sound a buzzer which I'll connect to another GPIO pin. This will be a brief audible indication that the command has been executed, as there is not necessarily anything on screen.

# Now wait!
while 1:
    time.sleep(1)
