from machine import Pin
from time import sleep
import dht

sensor = dht.DHT22(Pin(26))

while True:
  try:
    sensor.measure()     # Recovers measurements from the sensor
    print(f"Temperature : {sensor.temperature():.1f}°C")
    print(f"Humidity    : {sensor.humidity():.1f}%")
    sleep(2)             # the DHT22 returns at most one measurement every 2s, so we wait 2 seconds before reading again
  except OSError as e:
    print("Failed reception")