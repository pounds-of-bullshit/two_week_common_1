def task1():
import pandas as pd
import matplotlib.pyplot as plt
import requests

    # Reads the client ID from a text file
client_id = open(r"C:\Users\ashle\OneDrive - Norwegian University of Life Sciences\INF201\client-ID.txt").read().strip()

# Defines the endpoint and parameters for the API request
endpoint = "https://frost.met.no/observations/v0.jsonld"
parameters = {
    "sources": "SN17850",
    "elements": "mean(air_temperature P1D)",
    "referencetime": "2025-01-01/2025-12-31",
}

# The API request is then sent using the get function from the requests package
frost_response = requests.get(endpoint, parameters, auth=(client_id, ""))
# Returns a status code to check if it went well, 200 means that it did
assert frost_response.status_code == 200 

# Converts it to JSON format
frost_data = frost_response.json()

# Extracts the relevant data and temperature from each observation
temp_data = [{"Time": pd.to_datetime(entry["referenceTime"]), # Converts data to datetime
              "T_avg": entry["observations"][0]["value"]} # The 0 here means from the first observation
              for entry in frost_data["data"]] # Makes a loop through the API data

# Creates a DataFrame using pandas and uses the "Time" column as the index
T_df = pd.DataFrame.from_records(temp_data).set_index("Time")

# Plots the daily mean temperature
plt.figure(figsize=(12, 5))
plt.plot(T_df.index, T_df["T_avg"], label="Daily mean temperature")

plt.title("Daily mean temperature in Ås (2025)") # Adds the title
plt.xlabel("Time") # Labels the x-axis
plt.ylabel("Temperature (°C)") # The y-axis 
plt.axhline(0, color="black", linestyle="--", linewidth=1) # Adds a horizontal line at 0°C
plt.grid(True, alpha=0.3) # Adds grid lines
plt.tight_layout() # Adjusts the layout to prevent overlaping
plt.show() # Displays the plot

# Calculates the summary statistics for the temperature data
summary = pd.DataFrame({
    "Mean": [T_df["T_avg"].mean()],
    "Median": [T_df["T_avg"].median()],
    "Min": [T_df["T_avg"].min()],
    "Max": [T_df["T_avg"].max()],
}, index=["Temperature (°C):"])

# Prints out the summary with the variables rounded to 2 decimales
print("Temperature summary statistics for Ås (2025):")
print(summary.round(2))

