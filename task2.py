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

    plt.plot(task1_data_list, label="Temperature")
    plt.plot(task2_data_list, label="Precipitation")
    plt.legend()
    plt.show()
