from gpiozero import DistanceSensor
import time
import gate  
import lcddisplay
from time import sleep

trigPin = 20
echoPin = 21
sensor = DistanceSensor(echo=echoPin, trigger=trigPin, max_distance=3)

currentDistance = sensor.distance * 100  
gate_open = False  
last_open_time = 0  

def check_distance():
    global currentDistance, gate_open, last_open_time
    newDistance = sensor.distance * 100  # Convert to cm
    delta = abs(currentDistance - newDistance)

    if newDistance < 5 and not gate_open:
        lcddisplay.messagedisplay(f'Thank You!!','Gate Opening')
        gate.gateOpen()  
        gate_open = True
        last_open_time = time.time()
        print("Gate opened")
        sleep(4)
        lcddisplay.lcd1602.clear()



    if gate_open and (time.time() - last_open_time >= 5):
        lcddisplay.messagedisplay(f'Thank You!!','Gate Closing')
        gate.gateClose()  
        gate_open = False
        print("Gate closed")
        sleep(3)
        lcddisplay.lcd1602.clear()

    currentDistance = newDistance  

