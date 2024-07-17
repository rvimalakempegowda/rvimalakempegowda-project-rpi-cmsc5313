import smbus
from time import sleep, strftime
from datetime import datetime
from LCD1602 import CharLCD1602

lcd1602 = CharLCD1602()    

    
def messagedisplay(message,message2=None):
    lcd1602.init_lcd()
    count = 0
    lcd1602.clear()
    lcd1602.write(0, 0, message )
    if message2 is not None:
        lcd1602.write(0, 1, message2)  
    

    