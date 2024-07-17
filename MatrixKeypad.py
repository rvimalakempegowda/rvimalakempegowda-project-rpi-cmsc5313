
import Keypad   
import gate
from time import sleep
import lcddisplay
import camera_handler
ROWS = 4        
COLS = 4        
keys =  [   '1','2','3','A',    
            '4','5','6','B',
            '7','8','9','C',
            '*','0','#','D'     ]

# predefined names and passwords
password = {'Adam':'2406#','Richard':'1206#','Steve':'2805#','Kevin':'1904#'}

entrypin=''
rowsPins = [6, 13, 19, 26]    
colsPins = [10, 4, 23, 24]     

def gatePin():
    global entrypin
    keypad = Keypad.Keypad(keys,rowsPins,colsPins,ROWS,COLS)    
    keypad.setDebounceTime(50)      
    key = keypad.getKey()       
    if(key != keypad.NULL):     
        print ("You Pressed Key : %c "%(key))
        entrypin +=key
        lcddisplay.messagedisplay(f'Entered Pin:',entrypin)

        if len(entrypin)==5:
            checkPassword()

def checkPassword():
    global password
    global entrypin
    passwordmatch = False
    print(entrypin)
    for name,pin in password.items():
        if pin == entrypin:
            print(f'Welcome {name}')
            lcddisplay.messagedisplay(f'Welcome {name}','Gate Opening')
            gate.gateOpen()
            print("Image captured")
            camera_handler.capture()
            sleep(4)
            lcddisplay.lcd1602.clear()
            lcddisplay.messagedisplay('Gate Closing !!')
            gate.gateClose()
            sleep(2)
            lcddisplay.lcd1602.clear()
            entrypin = ''
            passwordmatch = True
       
    if passwordmatch == False:
        print('Wrong password entered')
        lcddisplay.messagedisplay('Wrong Password!!', 'Try Again')
        sleep(3)
        lcddisplay.lcd1602.clear()
        entrypin = ''