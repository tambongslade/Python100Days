import requests
angela_key = "69f04e4613056b159c261a9d9e664d2"
api_key = "cbd9abfcd459f40da67935c087edcc94"
My_lat = 3.848032
My_long = 11.502075
response = requests.get(url=f"https://api.openweathermap.org/data/3.0/onecall?lat={My_lat}&lon={My_long}&exclude=&appid={api_key}")
print(response.json())
from twilio.rest import Client

account_sid = "AC7775d7fcc9da8c2191415fd066b1b442"
auth_token = "52a966b01209af2c652d967dbdeaeee1"

client = Client(account_sid,auth_token)
try:
    message = client.messages \
        .create(
        body="I love you Baby is dudu, trying python things",
        from_='+12568294291',
        to = '+237670527426'
    )
except Exception as e :
    print(str(e))

print(message.status)
