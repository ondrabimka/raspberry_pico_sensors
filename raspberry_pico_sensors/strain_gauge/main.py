import machine
import utime

ANALOG_PIN = 26  # Replace with the actual ADC pin number

# Set up the ADC for reading the strain gauge
adc = machine.ADC(ANALOG_PIN)

# Calibration values
calibration_factor = 10.0  # Adjust this based on your calibration data
zero_force_voltage = 0.5   # Adjust this based on your calibration data

def read_strain():
    raw_value = adc.read_u16()  # Read the raw analog value

    # Convert the raw value to voltage
    voltage = (raw_value / 65535) * 3.3  # 16-bit ADC with a 3.3V reference voltage

    # Convert voltage to force using calibration data
    force = (voltage - zero_force_voltage) * calibration_factor

    return force

def main():
    while True:
        strain_force = read_strain()
        print("Strain Force:", strain_force, "N")  # Units could be different based on your calibration
        utime.sleep(1)

if __name__ == "__main__":
    main()