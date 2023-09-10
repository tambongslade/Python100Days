import requests
MY_LAT= 3.848032
MY_LONG = 11.502075
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()


data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0
}
response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
data =response.json()
response.raise_for_status()
sunrise =  data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset =  data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise.split("T")[1].split(":")[0])
from datetime import datetime
time_now = datetime.now()
print(time_now.date())
