applicationID ="9215f571"
NutritionIX_api = "ab7da5c85d427de8d9ca6861f3501f42"
Nutrition_endPoint ="https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_get = "https://api.sheety.co/100b2da41208f3b99428b5165227c1f1/myWorkouts/workouts"
sheety_token = "Bearer Slade2021"
import requests
from datetime import datetime
now =datetime.now()
date = now.strftime("%m/%d/%y")
time = now.strftime("%H:%M:%S")
print(time)
header = {
    "x-app-id": applicationID,
    "x-app-key": NutritionIX_api,
    "content-type": "application/json"
}
sheety_header = {
    "Authorization": sheety_token
}
query = input("tell me which exercise you did: ")
user_params = {
    "query": query,
    "gender": "male",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30
}
response = requests.post(headers=header,url=Nutrition_endPoint,json=user_params)
data = response.json()
for results in data["exercises"]:

    sheety_params = {
         "workout": {
            "date": date,
            "time": time,
            "exercise": results["name"].title(),
            "duration":results["duration_min"],
            "calories":results["nf_calories"]
        }



}
shetty_response = requests.post(url=sheety_get,json=sheety_params ,headers=sheety_header)
print(shetty_response.text)
