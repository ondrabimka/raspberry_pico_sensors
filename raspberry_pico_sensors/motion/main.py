from machine import Pin
import utime

pir_sensor = Pin(16, Pin.IN)
utime.sleep(2)

while True:
   if pir_sensor.value() == 1:
       print("Motion Detected")
       utime.sleep(3)
   else:
       print("No Motion")
       utime.sleep(1)
       
