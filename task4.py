def task4():
import pandas as pd
import requests
import yaml 

    # Defines a function to count heatwaves
def count_heatwaves(station, year):
    """Counts heatwaves for a given weather station and year"""
    parameters = {
        "sources": station,
        "elements": "max(air_temperature P1D)",
        "referencetime": f"{year}-01-01/{year}-12-31",
    }

    frost_response = requests.get(endpoint, parameters, auth=(client_id, ""))
    assert frost_response.status_code == 200

    frost_data = frost_response.json()

    # Extracts the date and maximum temperature from each observation
    max_temp_data = [{"Time": pd.to_datetime(entry["referenceTime"]),
                      "T_max": entry["observations"][0]["value"]}
                      for entry in frost_data["data"]]

    M_df = pd.DataFrame.from_records(max_temp_data).set_index("Time")
    # Sorts the observations by date to ensure chronological order
    M_df = M_df.sort_index()
    
    heatwaves = 0 # Sets the inital amount to 0
    consecutive_days = 0
    previous_date = None # Stores the previous date for comparison

    # Loops through the maximum temperature data to count heatwaves
    for date, temperature in M_df["T_max"].items():
        # Continues counting if temperature >= 27 °C and dates are consecutive
        if temperature >= 27 and (previous_date is None or (date - previous_date).days == 1):
            consecutive_days += 1
        # Resets the count if the dates are not consecutive 
        elif temperature >= 27:
            consecutive_days = 1
        # Resets the count again if the temperature is below 27 °C
        else:
            consecutive_days = 0
        # Counts a heatwave when there are at least five consecutive warm days
        if consecutive_days >= 5:
            heatwaves += 1
        # Updates the previous date
        previous_date = date

    # Creates a summary dictionary with the results
    summary = {"station": station, "year": year, "heatwaves": heatwaves}

    # Opens a YAML file to write "w" the summary data, and then closes it
    heatwaves_file = open("heatwaves.yml", "w", encoding="utf-8")
    yaml.safe_dump(summary, heatwaves_file, sort_keys=False)
    heatwaves_file.close()
    
    print(f"Number of heatwaves in {year}: {heatwaves}")
    print(summary)

# Calls the function to count for Ås in 2025 
heatwave_summary = count_heatwaves("SN17850", 2025)

