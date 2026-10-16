def task3(): 
import pandas as pd
import matplotlib.pyplot as plt
import requests

# Defines the parameters for the API request, here we needed the ones from year 1925
parameters = {
    "sources": "SN17850",
    "elements": "mean(air_temperature P1D)",
    "referencetime": "1925-01-01/1925-12-31",
}

frost_response = requests.get(endpoint, parameters, auth=(client_id, ""))
assert frost_response.status_code == 200

frost_data = frost_response.json()

historical_data = [{"Time": pd.to_datetime(entry["referenceTime"]),
                    "T_avg": entry["observations"][0]["value"]}
                   for entry in frost_data["data"]]

H_df = pd.DataFrame.from_records(historical_data).set_index("Time")

plt.figure(figsize=(12, 5))

# Plots temperatures from 2025 using the day of year
plt.plot(T_df.index.dayofyear, T_df["T_avg"], label="2025")
# Plot temperatures from 1925 using the day of year
plt.plot(H_df.index.dayofyear, H_df["T_avg"], color="red", label="1925")

plt.title("Daily mean temperature in Ås (1925 vs 2025)")
plt.xlabel("Day of year")
plt.ylabel("Temperature (°C)")
plt.axhline(0, color="black", linestyle="--", linewidth=1)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

# Calculates the summary statistics for both years 
summary = pd.DataFrame({
    "Mean": [H_df["T_avg"].mean(), T_df["T_avg"].mean()],
    "Median": [H_df["T_avg"].median(), T_df["T_avg"].median()],
    "Min": [H_df["T_avg"].min(), T_df["T_avg"].min()],
    "Max": [H_df["T_avg"].max(), T_df["T_avg"].max()],
}, index=["1925 (°C):", "2025 (°C):"])

print("Temperature summary statistics for Ås (1925 vs 2025):")
print(summary.round(2))

