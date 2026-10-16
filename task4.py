import requests as rq


def task4_data(client_ID: str) -> list:
    endpoint = 'https://frost.met.no/observations/v0.jsonld'
    parameters = {
        'sources': 'SN17850',
        'elements': 'max(air_temperature P1D)',
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
        date = [item['referenceTime']]
        data_list.append([data[0], date])
    return data_list


def task4(client_ID):
    task4_data_list = task4_data(client_ID)

    saved_dates = []

    for index, day in enumerate(task4_data_list):
        if day[0] >= 27:
            if task4_data_list[index][0] >= 27 and task4_data_list[index+1][0] >= 27 and task4_data_list[index+2][0] >= 27 and task4_data_list[index+3][0] >= 27 and task4_data_list[index+4][0] >= 27:
                saved_dates.append([task4_data_list[index][1], task4_data_list[index+4][1]])

    print_date_list = []

    for date in saved_dates:
        start_date = date[0][0]
        end_date = date[1][0]

        start_date_string = f"{start_date[0]+start_date[1]+start_date[2]+start_date[3]+start_date[4]+start_date[5]+start_date[6]+start_date[7]+start_date[8]+start_date[9]}"
        end_date_string = f"{end_date[0]+end_date[1]+end_date[2]+end_date[3]+end_date[4]+end_date[5]+end_date[6]+end_date[7]+end_date[8]+end_date[9]}"

        print_date_list.append([start_date_string, end_date_string])
