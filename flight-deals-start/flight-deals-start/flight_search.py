from flight_data import FlightData
import requests
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    flight = FlightData()
    def __init__(self,data :flight.sheet_Data):
        teq_url = "https://api.tequila.kiwi.com/locations/"
        header = {
            "api_key": "BgJ5BEx6jx0jtPJOHmXE0OkgkwmX9QBa",
        }
        parms = {

            "term": {
                "name": data["city"]
            }
        }
        response = requests.get(url=teq_url,headers=header)
        print(response.text)




