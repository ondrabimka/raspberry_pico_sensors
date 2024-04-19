import machine
import utime

sensor_pin = machine.Pin(28)  # Change this to the correct pin number

try:
    print("Reading Soil Moisture...")
    utime.sleep(2)

    while True:
        
        adc = machine.ADC(sensor_pin)
        raw_value = adc.read_u16()

        # Convert the raw ADC reading to a percentage value (assuming a linear relationship)
        # Adjust the mapping based on your sensor's characteristics
        # Replace 0 and 65535 with the minimum and maximum raw readings you get from your sensor
        moisture_percentage = ((raw_value - 0) / (65535 - 0)) * 100
        print("Soil Moisture:", "{:.2f}%".format(moisture_percentage))
        utime.sleep(1)

except KeyboardInterrupt:
    print("Program terminated.")