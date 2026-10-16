def task5():
import pandas as pd
import matplotlib.pyplot as plt
import requests

def moving_average(temperature_data):
    """Calculate the 7-day moving average of temperature data"""
    # Returns the mean of seven (window=7) temperature measurements
    return temperature_data.rolling(window=7).mean()

# Sorts the temperatures by date
T_df = T_df.sort_index()

# Creates a new column with the 7-day moving average
T_df["Moving_avg"] = moving_average(T_df["T_avg"])

plt.figure(figsize=(12, 5))

# Plots daily mean temperatures as points in a size of 5
plt.scatter(T_df.index, T_df["T_avg"], s=5, label="Daily mean temperature") 

# Plots the 7-day moving average as a red line
plt.plot(T_df.index, T_df["Moving_avg"], color="red", label="7-day moving average temperature")

plt.title("Daily mean temperature and 7-day moving average in Ås (2025)")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.axhline(0, color="black", linestyle="--", linewidth=1)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
