
import Keypad   #import module Keypad
import gate
from time import sleep
import lcddisplay
ROWS = 4        # number of rows of the Keypad
COLS = 4        #number of columns of the Keypad
keys =  [   '1','2','3','A',    #key code
            '4','5','6','B',
            '7','8','9','C',
            '*','0','#','D'     ]

password = {'Adam':'2406#','Richard':'1206#','Steve':'2805#','Kevin':'1904#'}

entrypin=''
rowsPins = [6, 13, 19, 26]     #connect to the row pinouts of the keypad
colsPins = [10, 4, 23, 24]     #connect to the column pinouts of the keypad

def gatePin():
    global entrypin
    keypad = Keypad.Keypad(keys,rowsPins,colsPins,ROWS,COLS)    #creat Keypad object
    keypad.setDebounceTime(50)      #set the debounce time
    key = keypad.getKey()       #obtain the state of keys
    if(key != keypad.NULL):     #if there is key pressed, print its key code.
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
            lcddisplay.messagedisplay(f'Welcome {name}','Gate Openning')
            gate.gateOpen()
            sleep(4)
            lcddisplay.lcd1602.clear()
            lcddisplay.messagedisplay('Gate Closing !!')
            gate.gateClose()
            sleep(1)
            lcddisplay.lcd1602.clear()
            entrypin = ''
            passwordmatch = True
       
    if passwordmatch == False:
        print('Wrong password entered')
        entrypin = ''