import machine
import utime

# Set up ADC (Analog to Digital Converter) on GP26 pin
adc = machine.ADC(machine.Pin(26))

# Create a file to save the FSR data
data_file = open("fsr_data.txt", "w")

# Define the calibration parameters for your FSR
# These values need to be adjusted based on your FSR specifications
fsr_min_adc = 0
fsr_max_adc = 65535
force_min = 0
force_max = 100

try:
    while True:
        # Read analog value from FSR using ADC
        analog_value = adc.read_u16()

        # Convert the analog value to a force reading using linear scaling
        force = ((analog_value - fsr_min_adc) / (fsr_max_adc - fsr_min_adc)) * (force_max - force_min) + force_min

        # Get the current timestamp in microseconds
        timestamp_us = utime.ticks_us()

        # Save the timestamp and force reading to the data file
        data_file.write(f"Timestamp (us): {timestamp_us}, Force: {force}\n")
        data_file.flush()  # Make sure the data is written immediately

        print("Timestamp (us):", timestamp_us, "Force:", force)

        utime.sleep_ms(100)  # Adjust the delay as needed in milliseconds

except KeyboardInterrupt:
    # Close the data file when Ctrl+C is pressed
    data_file.close()
    print("Data file closed.")
