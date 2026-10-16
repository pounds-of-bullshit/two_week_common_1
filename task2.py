import task1 as t1
import requests as rq
import matplotlib.pyplot as plt


def task2_data(client_ID: str) -> list:
    endpoint = 'https://frost.met.no/observations/v0.jsonld'
    parameters = {
        'sources': 'SN17850',
        'elements': 'sum(precipitation_amount P1D)',
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


def task2(client_ID):
    task1_data_list = t1.task1_data(client_ID)
    task2_data_list = task2_data(client_ID)

    # Creates a figure with two y-axes 
    fig, ax1 = plt.subplots(figsize=(12, 5))

    ax1.plot(task1_data_list, label="Daily mean temperature")
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Temperature (°C)")
    ax1.axhline(0, color="black", linestyle="--", linewidth=1)
    ax1.tick_params(axis="y")  # Sets the tick parameters for the first y-axis

    # Create a second y-axis sharing the same x-axis
    ax2 = ax1.twinx()

    ax2.bar(range(len(task2_data_list)), height=task2_data_list, color="red", label="Daily precipitation")

    ax2.set_ylabel("Precipitation (mm)")
    ax2.tick_params(axis="y")
    ax2.set_ylim(bottom=0) # Sets the lower limit of the second y-axis to 0

    plt.title("Daily mean temperature and precipitation in Ås (2025)")
    ax1.grid(True, alpha=0.3)
    ax1.legend(loc="upper left")
    ax2.legend(loc="upper right")
    plt.tight_layout()
    plt.show()
