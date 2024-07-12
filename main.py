import touch
import temp
import time
import touch1
import photo
import MatrixKeypad
from signal import pause


while True:
    MatrixKeypad.gatePin()
    touch.touch()
    touch1.touch1()
    # temp.temperature_humidity()
    # photo.photoresistor()
    time.sleep(0.003)

pause()