from machine import Pin, ADC
import time

ANALOG_IN_PIN = 26  # Replace with the actual pin number for analog input
DIGITAL_IN_PIN = 16  # Replace with the actual pin number for digital input

analogPin = ADC(Pin(ANALOG_IN_PIN))
digitalPin = Pin(DIGITAL_IN_PIN, Pin.IN)

def read_inputs():
    analog_value = analogPin.read_u16()
    digital_value = digitalPin.value()
    return analog_value, digital_value

def main():
    while True:
        analog_value, digital_value = read_inputs()
        print("Analog Input:", analog_value)
        print("Digital Input:", digital_value)
        print("-------------------")
        time.sleep_ms(20)

if __name__ == "__main__":
    main()


