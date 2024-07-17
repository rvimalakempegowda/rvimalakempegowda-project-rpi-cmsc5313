from gpiozero import RGBLED
from sensor import TouchSensor
import time
sensorPin = 12 
sensor = TouchSensor(sensorPin, pull_up=False)
led = RGBLED(red=9, green=15, blue=14, active_high=False)  

import firebase_setup
import constant


collection = firebase_setup.db.collection(constant.COLLECTION_NAME)
doc_slot2_ref = collection.document(constant.DOCUMENT_PARKING)

grade=0

def SensorEvent(): # When Sensor is pressed, this function will be executed
    global grade
    grade=grade+1
    print(grade)
    if(grade > 1):
        grade=0
    if grade==1:
        led.color = (1, 0, 0)
        doc_slot2_ref.update({'slot2': True})  
        print('updating to firebase true')      
    else:
        led.color = (0, 1, 0) 
        doc_slot2_ref.update({'slot2': False})
        print('updating to firebase false')       


def touch1():
    sensor.when_touch = SensorEvent
    sensor.when_no_touch = SensorEvent
    # print("running")
    global grade
    if grade==1:
        led.color = (1, 0, 0)      
    else:
        led.color = (0, 1, 0) 

  

def destroy():
    led.close()
    sensor.close() 