import touch
import temp
import time
import touch1
import MatrixKeypad
from signal import pause
import photoresistor
import distance_sensor  

def main_loop():
    last_temp_check = time.time()
    last_photo_check = time.time()
    check_interval = 60  # Interval to check temperature, humidity, and photoresistor (in seconds)
    
    # Setup the ADC for photoresistor
    photoresistor.setup_adc()

    while True:
        try:
            # Handle gate pin actions using the matrix keypad
            MatrixKeypad.gatePin()

            # Process touch inputs
            touch.touch()
            touch1.touch1()

            # Check if it's time to read temperature and humidity
            current_time = time.time()
            if current_time - last_temp_check >= check_interval:
                print("Checking temperature and humidity...")
                temp.temperature_humidity()
                last_temp_check = current_time

            # Check if it's time to read the photoresistor
            if current_time - last_photo_check >= check_interval:
                print("Checking photoresistor...")
                photoresistor.read_photoresistor()
                last_photo_check = current_time

            # Check the distance sensor continuously
            distance_sensor.check_distance()

            # Short sleep to prevent high CPU usage
            time.sleep(0.01)

        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(1)  # Add a delay to avoid rapid repeated errors

if __name__ == "__main__":
    print('Program is starting ...')
    try:
        main_loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        photoresistor.destroy_adc()
        print("Ending program")
    pause()
