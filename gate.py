#!/usr/bin/env python3
########################################################################
# Filename    : Sweep.py
# Description : Servo sweep
# Author      : www.freenove.com
# modification: 2023/05/12
########################################################################
from gpiozero import AngularServo
import time
 
myGPIO=16
SERVO_DELAY_SEC = 0.001 
myCorrection=0.0
maxPW=(2.5+myCorrection)/1000
minPW=(0.5-myCorrection)/1000
servo =  AngularServo(myGPIO,initial_angle=0,min_angle=0, max_angle=180,min_pulse_width=minPW,max_pulse_width=maxPW)

def gateOpen():
    for angle in range(0, 181, 1):   # make servo rotate from 0 to 180 deg
        servo.angle = angle
        time.sleep(SERVO_DELAY_SEC)

def gateClose():
    for angle in range(180, -1, -1): # make servo rotate from 180 to 0 deg
        servo.angle = angle
        time.sleep(SERVO_DELAY_SEC)

