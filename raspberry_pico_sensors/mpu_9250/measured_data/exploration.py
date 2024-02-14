# %%
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd

gyro_data = pd.read_csv("raspberry_pico_sensors/mpu_9250/measured_data//gyro_data.txt", names=["timestamp","x","y","z"], dtype={"timestamp":int, "x":float, "y": float, "z": float})
gyro_data[['x','y','z']].plot(subplots=True)
# %%

acc_data = pd.read_csv("raspberry_pico_sensors/mpu_9250/measured_data/acceleration_data.txt", names=["timestamp","x","y","z"], dtype={"timestamp":int, "x":float, "y": float, "z": float})
acc_data[['x','y','z']].plot(subplots=True)
# %%
