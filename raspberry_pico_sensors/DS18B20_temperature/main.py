# Import necessary modules
import machine, onewire, ds18x20, time

# Define the pin for the DS18B20 temperature sensor
ds_pin = machine.Pin(22)

# Initialize the DS18X20 sensor using the OneWire protocol
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

# Scan for DS18B20 temperature sensors on the OneWire bus
roms = ds_sensor.scan()
print('Found DS devices: ', roms)

# Main loop to continuously read temperature data
while True:
    # Initiate temperature conversion for all DS18B20 sensors
    ds_sensor.convert_temp()

    # Wait for the conversion to complete (750 milliseconds for DS18B20)
    time.sleep_ms(750)

    # Iterate over each DS18B20 sensor found
    for rom in roms:
        print(rom)

        # Read temperature in degrees Celsius from the sensor
        tempC = ds_sensor.read_temp(rom)

        # Print the temperature in a formatted manner
        print('Temperature (ºC):', "{:.2f}".format(tempC))

    # Wait for a period (3 seconds in this case) before starting the next iteration
    time.sleep(3)