import utime
from machine import I2C, Pin

# Assuming you have mpu6500.py in the same directory
from mpu6500 import MPU6500, SF_G, SF_DEG_S

i2c = I2C(0, scl=Pin(1), sda=Pin(0))
mpu6500 = MPU6500(i2c, accel_sf=SF_G, gyro_sf=SF_DEG_S)
offset = mpu6500.calibrate(count=10000, delay=0)

print("Offset: ", offset)

print("mpu6500 id: " + hex(mpu6500.whoami))

# Open files for writing
acceleration_file = open("acceleration_data.txt", "w")
gyro_file = open("gyro_data.txt", "w")
temperature_file = open("temperature_data.txt", "w")

try:
    while True:
        # Read sensor data
        acceleration = mpu6500.acceleration
        gyro = mpu6500.gyro
        temperature = mpu6500.temperature

        # Get current timestamp in milliseconds
        timestamp_ms = utime.ticks_ms()

        # Print sensor data to console with timestamp
        print(f"Timestamp: {timestamp_ms}, Acceleration: {acceleration}")
        print(f"Timestamp: {timestamp_ms}, Gyro: {gyro}")
        print(f"Timestamp: {timestamp_ms}, Temperature: {temperature}")

        # Write sensor data to files with timestamp
        acceleration_file.write(f"{timestamp_ms},{acceleration[0]},{acceleration[1]},{acceleration[2]}\n")
        gyro_file.write(f"{timestamp_ms}, {gyro[0]}, {gyro[1]}, {gyro[2]}\n")
        temperature_file.write(f"{timestamp_ms}, {temperature}\n")

        utime.sleep_ms(100)

except KeyboardInterrupt:
    # Close files when Ctrl+C is pressed
    acceleration_file.close()
    gyro_file.close()
    temperature_file.close()
    print("Files closed.")
