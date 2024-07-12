#!/usr/bin/env python3
########################################################################
# Filename    : UltrasonicRanging.py
# Description : Get distance via UltrasonicRanging sensor
# auther      : www.freenove.com
# modification: 2023/05/13
########################################################################
from gpiozero import DistanceSensor
from time import sleep

trigPin = 20
echoPin = 21
sensor = DistanceSensor(echo=echoPin, trigger=trigPin ,max_distance=3)

def loop():
    print('Distance: ', sensor.distance * 100,'cm')

