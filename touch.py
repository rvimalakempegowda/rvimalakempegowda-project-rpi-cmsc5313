from gpiozero import RGBLED
from sensor import TouchSensor
import time
sensorPin = 18 
sensor = TouchSensor(sensorPin, pull_up=False)
led = RGBLED(red=27, green=22, blue=5,active_high=False)  

import firebase_setup
import constant


collection = firebase_setup.db.collection(constant.COLLECTION_NAME)
doc_slot1_ref = collection.document(constant.DOCUMENT_PARKING)

grade=0

def SensorEvent(): # When Sensor is pressed, this function will be executed
    global grade
    grade=grade+1
    print(grade)
    if(grade > 1):
        grade=0
    if grade==1:
        led.color = (1, 0, 0)
        doc_slot1_ref.update({'slot1': True})  
        print('updating to firebase true')      
    else:
        led.color = (0, 1, 0) 
        doc_slot1_ref.update({'slot1': False})
        print('updating to firebase false')      


def touch():
    sensor.when_touch = SensorEvent
    sensor.when_no_touch = SensorEvent
   
    global grade
    if grade==1:
        led.color = (1, 0, 0)      
    else:
        led.color = (0, 1, 0) 

  

def destroy():
    led.close()
    sensor.close() 

  