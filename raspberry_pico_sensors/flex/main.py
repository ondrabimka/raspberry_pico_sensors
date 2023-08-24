import machine
import time

VCC = 3.3
R_DIV = 10000.0
flatResistance = 25000.0
bendResistance = 100000.0

flexPin = 26  # Replace with the actual ADC pin number

adc = machine.ADC(machine.Pin(flexPin))

def read_flex():
    ADCflex = adc.read_u16()
    Vflex = ADCflex * VCC / 65535.0
    Rflex = R_DIV * (VCC / Vflex - 1.0)
    return Rflex

def calculate_bend_angle(resistance):
    angle = (resistance - flatResistance) / (bendResistance - flatResistance) * 90.0
    print("Angle:", angle)
    return max(0, min(90, angle))  # Ensure angle is within 0-90 degrees range

def main():
    while True:
        Rflex = read_flex()
        angle = calculate_bend_angle(Rflex)
        print("Resistance:", Rflex, "ohms")
        print("Bend:", angle, "degrees")
        print()
        time.sleep(0.5)

if __name__ == "__main__":
    main()