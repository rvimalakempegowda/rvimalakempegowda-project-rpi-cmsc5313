from gpiozero import PWMLED
import time
from ADCDevice import *

ledPin = 25 
led = PWMLED(ledPin)
adc = ADCDevice() 

def setup_adc():
    global adc
    if(adc.detectI2C(0x48)): # Detect the pcf8591.
        adc = PCF8591()
    elif(adc.detectI2C(0x4b)): # Detect the ads7830
        adc = ADS7830()
    else:
        print("No correct I2C address found, \n"
              "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
              "Program Exit. \n")
        exit(-1)

def read_photoresistor():
    value = adc.analogRead(0)    
    led.value = value / 255.0    
    voltage = value / 255.0 * 3.3
    print ('ADC Value : %d, Voltage : %.2f' % (value, voltage))

def destroy_adc():
    led.close()
    adc.close()
