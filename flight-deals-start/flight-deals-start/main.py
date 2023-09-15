# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_data import FlightData
from flight_search import FlightSearch
from flight_search import FlightSearch
from data_manager import DataManager

flight_data = FlightData()

for data in flight_data.sheet_Data:
    FlightSearch(data)
    print(data)
    manager = DataManager(data)
