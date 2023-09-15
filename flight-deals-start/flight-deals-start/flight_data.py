import requests
from pprint import pprint


class FlightData:
    # This class is responsible for structuring the flight data.

    def __init__(self):
        self.sheet_Data = []
        tiquilo_api = "https://api.tequila.kiwi.com/v2"
        sheety_api = "https://api.sheety.co/100b2da41208f3b99428b5165227c1f1/flightDeals/prices"
        tiquilo_params = {

        }

        response = requests.get(url=sheety_api)
        data = response.json()["prices"]
        for dat in data:
            self.sheet_Data.append(dat)

