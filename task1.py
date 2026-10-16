import requests as rq
import matplotlib.pyplot as plt
import tkinter as tk
import numpy as np


def task1_data(client_ID: str) -> list:
    endpoint = 'https://frost.met.no/observations/v0.jsonld'
    parameters = {
        'sources': 'SN17850',
        'elements': 'mean(air_temperature P1D)',
        'referencetime': '2025-01-01/2025-12-31',
    }
    # Issue an HTTP GET request
    r = rq.get(endpoint, parameters, auth=(client_ID, ''))
    # Extract JSON data
    json_file = r.json()
    hey = json_file["data"]
    data_list = []
    for index, item in enumerate(hey):
        data = [obs['value'] for obs in item['observations']]
        data_list.append(data[0])
    return data_list


def task1(client_ID):
    data_list = task1_data(client_ID)

    # plot the data
    plt.title("Daily mean temperature in Ås (2025)")  # Adds the title
    plt.xlabel("Time")  # Labels the x-axis
    plt.ylabel("Temperature (°C)")  # The y-axis 
    plt.axhline(0, color="black", linestyle="--", linewidth=1)  # Adds a horizontal line at 0°C
    plt.grid(True, alpha=0.3)  # Adds grid lines
    plt.tight_layout()  # Adjusts the layout to prevent overlaping
    plt.plot(data_list)
    plt.show()

    # summary table
    summary_table = tk.Tk()

    summary_table.title("Task 1 summary table")
    summary_table.geometry("350x200")

    tk.Label(summary_table,
             text="Temperature summary statistics for Ås (2025):",
             font=("Arial", 10)).grid(row=1)
    tk.Label(summary_table,
             text=f"Mean: {np.mean(data_list):.1f}",
             font=("Arial", 10)).grid(row=2)
    tk.Label(summary_table,
             text=f"Median: {np.median(data_list)}",
             font=("Arial", 10)).grid(row=3)
    tk.Label(summary_table,
             text=f"Max: {max(data_list)}",
             font=("Arial", 10)).grid(row=4)
    tk.Label(summary_table,
             text=f"Min: {min(data_list)}",
             font=("Arial", 10)).grid(row=5)
