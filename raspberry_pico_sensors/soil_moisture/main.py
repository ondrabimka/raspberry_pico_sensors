import machine
import utime

sensor_pin = machine.Pin(28)  # Change this to the correct pin number
adc = machine.ADC(sensor_pin)

def read_soil_moisture():
    # Read analog value from ADC
    output = adc.read_u16()

    # Print raw analog value for troubleshooting
    print("Raw Analog Value:", output)

# Main loop to continuously read and print soil moisture values
try:
    print("Reading From the Sensor ...")
    utime.sleep(2)

    while True:
        read_soil_moisture()
        utime.sleep(1)

except KeyboardInterrupt:
    print("Program terminated.")