import requests
from datetime import datetime
import  time

MY_LAT = 3.848032 # Your latitude
MY_LONG = 11.502075 # Your longitude
email = "tambongslade17@gmail.com"
password = "lydkfckhbqjhfryf"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

time_now = datetime.now().hour
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    if time_now>= sunset or time_now<=sunrise:
        return True
def ISSOverHead():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunset)
    print(sunrise)

    #If the ISS is close to my current position
    if -2 <= iss_latitude<= 8 and 6<= iss_longitude <= 16:
        return True
# and it is curren tly dark

import smtplib
# Then send me an email to tell me to look up.

while True:
    time.sleep(60)
    if is_night() and ISSOverHead():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(to_addrs=email,
                            from_addr=email,
                            msg="Subject:Look UP👍\n\n The ISS is above you in the sky ")

# BONUS: run the code every 60 seconds.



