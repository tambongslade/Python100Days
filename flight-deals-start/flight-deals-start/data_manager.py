import requests
from flight_data import FlightData


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    flight = FlightData()

    def __init__(self, data: flight.sheet_Data):
        Sheety_put = f"https://api.sheety.co/100b2da41208f3b99428b5165227c1f1/flightDeals/prices/{data['id']}"
        Bode = {
            "price":{
                "iataCode": data["iataCode"]

            }
        }
        response = requests.put(url=Sheety_put,json=Bode)
        print(response.text)


