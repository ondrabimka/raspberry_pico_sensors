import machine
import utime

# Set up ADC (Analog to Digital Converter) on GP26 pin
adc = machine.ADC(machine.Pin(26))

# Create a file to save the EKG data
data_file = open("ekg_data.txt", "w")

try:
    while True:
        # Get the current timestamp in microseconds
        timestamp_us = utime.ticks_us()

        # Read analog value from ADC
        analog_value = adc.read_u16()

        # Convert the analog value to voltage (assuming 3.3V reference)
        voltage = (analog_value / 65535) * 3.3

        # Save the timestamp and voltage to the data file
        data_file.write(f"{timestamp_us},{voltage}\n")
        data_file.flush()  # Make sure the data is written immediately

        print("Timestamp (us):", timestamp_us, "Voltage:", voltage)

        utime.sleep_us(5000)  # Adjust the delay as needed in microseconds. This should be ok for EKg sampling based on NS-theorem

except KeyboardInterrupt:
    # Close the data file when Ctrl+C is pressed
    data_file.close()
    print("Data file closed.")
