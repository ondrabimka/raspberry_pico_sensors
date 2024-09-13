import machine 
import time
from machine import Pin

adc = machine.ADC(26)
conversion_factor = 100 / (65535)

while True:
    value = 100 - (adc.read_u16() * conversion_factor)
    print(round(value, 1), "%")
    time.sleep(1)