import pandas as pd
import matplotlib.pyplot as plt
import requests


def task5(client_ID):
    def moving_average(temperature_data):
        """Calculate the 7-day moving average of temperature data"""
        # Returns the mean of seven (window=7) temperature measurements
        return temperature_data.rolling(window=7).mean()

    # Defines the endpoint and parameters for the API request
    endpoint = "https://frost.met.no/observations/v0.jsonld"
    parameters = {
        "sources": "SN17850",
        "elements": "mean(air_temperature P1D)",
        "referencetime": "2025-01-01/2025-12-31",
    }

    # The API request is then sent using the get function from the requests package
    frost_response = requests.get(endpoint, parameters, auth=(client_ID, ""))
    # Returns a status code to check if it went well, 200 means that it did
    assert frost_response.status_code == 200

    # Converts it to JSON format
    frost_data = frost_response.json()

    # Extracts the relevant data and temperature from each observation
    temp_data = [{"Time": pd.to_datetime(entry["referenceTime"]),  # Converts data to datetime
                  "T_avg": entry["observations"][0]["value"]}  # The 0 here means from the first observation
                 for entry in frost_data["data"]]  # Makes a loop through the API data

    # Creates a DataFrame using pandas and uses the "Time" column as the index
    T_df = pd.DataFrame.from_records(temp_data).set_index("Time")

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
