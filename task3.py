import task1 as t1
import requests as rq
import matplotlib.pyplot as plt
import tkinter as tk
import numpy as np


def task3_data(client_ID: str) -> list:
    endpoint = 'https://frost.met.no/observations/v0.jsonld'
    parameters = {
        'sources': 'SN17850',
        'elements': 'mean(air_temperature P1D)',
        'referencetime': '1925-01-01/1925-12-31',
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


def task3(client_ID):
    task1_data_list = t1.task1_data(client_ID)
    task3_data_list = task3_data(client_ID)

    plt.plot(task1_data_list, label="Temperature 2025")
    plt.plot(task3_data_list, label="Temperature 1925")
    plt.legend()
    plt.show()

    summary_table = tk.Tk()

    summary_table.title("Task 1 summary table")
    summary_table.geometry("350x200")

    tk.Label(summary_table,
             text="Temperature summary table",
             font=("Arial", 10)).grid(row=1, column=1)

    tk.Label(summary_table,
             text="2025",
             font=("Arial", 10)).grid(row=2, column=1)
    tk.Label(summary_table,
             text=f"Mean: {np.mean(task1_data_list):.1f}",
             font=("Arial", 10)).grid(row=3, column=1)
    tk.Label(summary_table,
             text=f"Median: {np.median(task1_data_list)}",
             font=("Arial", 10)).grid(row=4, column=1)
    tk.Label(summary_table,
             text=f"Max: {max(task1_data_list)}",
             font=("Arial", 10)).grid(row=5, column=1)
    tk.Label(summary_table,
             text=f"Min: {min(task1_data_list)}",
             font=("Arial", 10)).grid(row=6, column=1)

    tk.Label(summary_table,
             text="1925",
             font=("Arial", 10)).grid(row=2, column=2)
    tk.Label(summary_table,
             text=f"Mean: {np.mean(task3_data_list):.1f}",
             font=("Arial", 10)).grid(row=3, column=2)
    tk.Label(summary_table,
             text=f"Median: {np.median(task3_data_list)}",
             font=("Arial", 10)).grid(row=4, column=2)
    tk.Label(summary_table,
             text=f"Max: {max(task3_data_list)}",
             font=("Arial", 10)).grid(row=5, column=2)
    tk.Label(summary_table,
             text=f"Min: {min(task3_data_list)}",
             font=("Arial", 10)).grid(row=6, column=2)
