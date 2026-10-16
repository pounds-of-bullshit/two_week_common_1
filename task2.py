def task2():
import pandas as pd
import matplotlib.pyplot as plt
import requests

# Defines the parameters for the API request, here we needed the daily precipation
parameters = {
    "sources": "SN17850",
    "elements": "sum(precipitation_amount P1D)",
    "referencetime": "2025-01-01/2025-12-31",
}

frost_response = requests.get(endpoint, parameters, auth=(client_id, ""))
assert frost_response.status_code == 200

frost_data = frost_response.json()

# Extracts the relevant data and precipitation from each observation
precipitation_data = [{"Time": pd.to_datetime(entry["referenceTime"]),
                       "Precipitation": entry["observations"][0]["value"]}
                       for entry in frost_data["data"]]

P_df = pd.DataFrame.from_records(precipitation_data).set_index("Time")

# Creates a figure with two y-axes 
fig, ax1 = plt.subplots(figsize=(12, 5))

# Plots daily mean temperature on the first y-axis
ax1.plot(T_df.index, T_df["T_avg"], label="Daily mean temperature")

ax1.set_xlabel("Time")
ax1.set_ylabel("Temperature (°C)")
ax1.axhline(0, color="black", linestyle="--", linewidth=1)
ax1.tick_params(axis="y") # Sets the tick parameters for the first y-axis

# Create a second y-axis sharing the same x-axis
ax2 = ax1.twinx()

# Plots the precipitation as red bars
ax2.bar(P_df.index, P_df["Precipitation"], color="red", alpha=0.6, label="Daily precipitation")

ax2.set_ylabel("Precipitation (mm)")
ax2.tick_params(axis="y")
ax2.set_ylim(bottom=0) # Sets the lower limit of the second y-axis to 0

plt.title("Daily mean temperature and precipitation in Ås (2025)")
ax1.grid(True, alpha=0.3)
ax1.legend(loc="upper left")
ax2.legend(loc="upper right")
plt.tight_layout()
plt.show()