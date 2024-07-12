# from gpiozero import RGBLED
# from sensor import TouchSensor
# import time


# led = RGBLED(red=13, green=19, blue=26, active_high=False)     # define ledPin
# sensorPin = 18     # define sensorPin
 
# sensor = TouchSensor(sensorPin, pull_up=False)
# grade=0

# # Define the functions that will be called when the line is
# # def SensorEvent():
# #     global  grade
# #     grade=grade+1
# #     print("Sensor is pressed!")
# #     if(grade > 3):
# #         grade=0
# def ledOnred():
#     print('red on')
#     led.green=0
#     led.red = 1
# def ledOngreen():
#     print('green on')
#     led.red = 0
#     led.green = 1

# def loop():

#     sensor.wait_for_touch =ledOngreen()
#     sensor.when_touch =ledOnred()
#     while True:
#         time.sleep(1)
#     #     global grade
#     #     if grade==1:
#     #         dc=35
#     #         led.red = dc / 100.0     # set dc value as the duty cycle
#     #     elif grade==2:
#     #         dc=65
#     #         led.green = dc / 100.0     # set dc value as the duty cycle
#     #     elif grade==3:
#     #         dc=100
#     #         led.blue = dc / 100.0     # set dc value as the duty cycle
#     #     else :
#     #         dc=0
#     #         led.red = dc / 100.0     # set dc value as the duty cycle

# def destroy():
#     led.close() 
#     sensor.close()                     

# if __name__ == '__main__':     # Program entrance
#     print ('Program is starting...')
#     try:
#         loop()
#     except KeyboardInterrupt:  # Press ctrl-c to end the program.
#         destroy()
#         print("Ending program")

from gpiozero import RGBLED
from sensor import TouchSensor
import time
sensorPin = 18 # define sensorPin
sensor = TouchSensor(sensorPin, pull_up=False)
led = RGBLED(red=27, green=22, blue=5,active_high=False) # define the pins for 

grade=0

def SensorEvent(): # When Sensor is pressed, this function will be executed
    global grade
    grade=grade+1
    print(grade)
    if(grade > 1):
        grade=0

def touch():
    sensor.when_touch = SensorEvent
    sensor.when_no_touch = SensorEvent
    # print("running")
    global grade
    if grade==1:
        led.color = (1, 0, 0)
        # print ('The current color is red')        
    else:
        led.color = (0, 1, 0) 
        # print ('The current color is green')
  

def destroy():
    led.close()
    sensor.close() 

  