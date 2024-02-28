import requests
from twilio.rest import Client
import os

account_sid = "YOUR_SID"
auth_token = "YOUR_TOKEN"

#I preferred to store it in environ.
api_key = os.environ.get('MY_API_KEY')

parameters = {
    "lat": "YOUR_LOCATION_LAT",
    "lon": "YOUR_LOCATION_LON",
    "appid": api_key,
    "cnt": 4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast?", params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔",
        from_= "YOUR_TWILIO_NUMBER",
        to= "YOUR_NUMBER",
    )

print(message.status)