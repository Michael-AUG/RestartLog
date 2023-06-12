#!/bin/python
# Simple script for restarting the rigctl.service and log.service services at the press of a button.
# by Michael Topple GM5AUG

import RPi.GPIO as GPIO
import time
import os

# Use the Broadcom SOC Pin numbers
# Setup the Pin with Internal pullups enabled and PIN in reading mode.
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# What to do when the button is pressed
def LogRestart(channel):
    os.system("sudo systemctl restart log.service rigctld.service")

# What to execute when the button pressed event happens
GPIO.add_event_detect(18, GPIO.FALLING, callback = LogRestart, bouncetime = 2000)

# Now wait!
while 1:
    time.sleep(1)
