# %%
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("raspberry_pico_sensors\ekg_heartbeat\exploration\ekg_data.txt", names=['Timestamp','HeartSignal'])

# %% Convert Timestamps to Datetime Objects
df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='us')


# %%
# Basic statistics
mean_signal = df['HeartSignal'].mean()
max_signal = df['HeartSignal'].max()
min_signal = df['HeartSignal'].min()

# Plot the heart signal
plt.figure(figsize=(12, 6))
plt.plot(df['HeartSignal'], label='Heart Signal', color='blue')
plt.axhline(y=mean_signal, color='red', linestyle='--', label=f'Mean: {mean_signal:.2f}')
plt.axhline(y=max_signal, color='green', linestyle='--', label=f'Max: {max_signal:.2f}')
plt.axhline(y=min_signal, color='purple', linestyle='--', label=f'Min: {min_signal:.2f}')
plt.xlabel('time')
plt.ylabel('Heart Signal')
plt.title('Heart Signal Analysis')
plt.legend()
plt.grid(True)
plt.show()
# %% Heart Rate Calculation

# Calculate time intervals between consecutive heartbeats
df['TimeDiff'] = df['Timestamp'].diff().dt.total_seconds()

# Calculate heart rate (beats per minute)
df['HeartRate'] = 60 / df['TimeDiff']

# Calculate average heart rate
average_heart_rate = df['HeartRate'].mean()
print(f'Average Heart Rate: {average_heart_rate:.2f} BPM')

# %% Heart Rate Variability (HRV)

# Compute SDNN (Standard Deviation of RR intervals)
sdnn = df['TimeDiff'].std()
print(f'SDNN (ms): {sdnn:.2f}')

# Compute RMSSD (Root Mean Square of Successive Differences)
rmssd = ((df['TimeDiff'] ** 2).mean()) ** 0.5
print(f'RMSSD (ms): {rmssd:.2f}')

# %% Visualize HRV Metrics:

# Plot histogram of RR intervals
plt.figure(figsize=(12, 6))
plt.hist(df['TimeDiff'], bins=20, edgecolor='black', color='lightblue')
plt.xlabel('RR Interval (s)')
plt.ylabel('Frequency')
plt.title('Distribution of RR Intervals')
plt.grid(True)
plt.show()


# %% Smooth the Heart Signal

# Define the window size for the moving average filter
window_size = 3  # You can adjust this as needed

# Apply the moving average filter
df['SmoothedSignal'] = df['HeartSignal'].rolling(window=window_size).mean()

# Plot the original and smoothed heart signals
plt.figure(figsize=(12, 6))
plt.plot(df['Timestamp'], df['HeartSignal'], label='Original Signal', color='blue', alpha=0.5)
plt.plot(df['Timestamp'], df['SmoothedSignal'], label=f'Smoothed Signal (Window Size {window_size})', color='red')
plt.xlabel('Timestamp')
plt.ylabel('Heart Signal')
plt.title('Heart Signal Analysis with Smoothing')
plt.legend()
plt.grid(True)
plt.show()

# %%
