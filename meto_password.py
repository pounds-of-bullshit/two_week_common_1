import tkinter as tk
import requests as rq

# ---client id and client secret input function, returns a list of client id and client secret---


def meto_login() -> list:

    def submit() -> None:

        client_ID_var = client_ID.get()
        client_secret_var = client_secret.get()

        try:
            endpoint = 'https://frost.met.no/observations/v0.jsonld'
            parameters = {
                'sources': 'SN18700,SN90450',
                'elements': 'mean(air_temperature P1D),sum(precipitation_amount P1D),mean(wind_speed P1D)',
                'referencetime': '2010-04-01/2010-04-03',
            }
            # Issue an HTTP GET request
            r = rq.get(endpoint, parameters, auth=(client_ID_var, ''))
            # Extract JSON data
            json_file = r.json()
            hey = json_file["data"]
            hey = hey
            print("Login worked.")
            id_input.destroy()
        except Exception as e:
            log_in_2 = tk.Label(id_input,
                                text="Server could not be reached or ID input wrong.",
                                font=("Arial", 10))
            log_in_2.grid(row=4)
            print(f"Error code is: {e}")

    id_input = tk.Tk()

    id_input.geometry("350x200")
    id_input.title("Credentials")
    label = tk.Label(id_input,
                     text="Please input your frost.met.no client ID and client secret.",
                     font=("Arial", 10))

    client_ID = tk.StringVar()
    client_secret = tk.StringVar()

    client_ID_entry = tk.Entry(id_input, textvariable=client_ID,
                               font=("Arial", 10))

    client_secret_entry = tk.Entry(id_input, textvariable=client_secret,
                                   font=("Arial", 10), show="*")

    sub_btn = tk.Button(id_input, text="Submit", command=submit)

    label.grid(row=0)
    client_ID_entry.grid(row=1)
    client_secret_entry.grid(row=2)
    sub_btn.grid(row=3)

    id_input.mainloop()

    return [client_ID.get(), client_secret.get()]
