import machine
import time

adcpin = 4
sensor = machine.ADC(adcpin)
  
while True:
    
    # Read the ADC value in u16 format
    adc_value = sensor.read_u16()
    
    # Convert the ADC value to voltage (V)
    volt = (3.3/65535) * adc_value
    
    # Convert the ADC value to temperature (°C) -> based on RP2040 datasheet
    temperature = 27 - (volt - 0.706) / 0.001721

    # Print the converted voltage and temperature values
    print(round(temperature, 1))
    
    time.sleep(1)