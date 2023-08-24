from machine import Pin
import time
 
pir = Pin(22, Pin.IN, Pin.PULL_DOWN)
n = 0
 
print('Starting up the PIR Module')
time.sleep(1)
print('Ready')
 
while True:
     if pir.value() == 1:
          n = n+1
          print('Motion Detected ',n)
     time.sleep(1)