from gpiozero import DistanceSensor
import time
import gate  # Assuming gate is a module controlling the gate
import lcddisplay
from time import sleep

trigPin = 20
echoPin = 21
sensor = DistanceSensor(echo=echoPin, trigger=trigPin, max_distance=3)

currentDistance = sensor.distance * 100  # Initialize currentDistance
gate_open = False  # Flag to track if the gate is open
last_open_time = 0  # Track the last time the gate was opened

def check_distance():
    global currentDistance, gate_open, last_open_time
    newDistance = sensor.distance * 100  # Convert to cm
    delta = abs(currentDistance - newDistance)

    if newDistance < 3 and not gate_open:
        lcddisplay.messagedisplay(f'Thank You!!','Gate Opening')
        gate.gateOpen()  # Open the gate if the distance is less than 3 cm
        gate_open = True
        last_open_time = time.time()
        print("Gate opened")
        sleep(4)
        lcddisplay.lcd1602.clear()


    # Check if the gate has been open for 10 seconds
    if gate_open and (time.time() - last_open_time >= 10):
        lcddisplay.messagedisplay(f'Thank You!!','Gate Closing')
        gate.gateClose()  
        gate_open = False
        print("Gate closed")
        sleep(3)
        lcddisplay.lcd1602.clear()

    currentDistance = newDistance  

