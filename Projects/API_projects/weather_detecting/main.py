import requests
from decouple import config
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = config("ACCOUNT_SID")  # Copied from my Dashboard remove config and write yours as a string
auth_token = config("AUTH_TOKEN")  # Copied from my Dashboard  remove config and write yours as a string


def bring_umberalla(data):
    first_12_hours = [data["hourly"][hour] for hour in range(0, 12)]
    weathers = [hour["weather"] for hour in first_12_hours]
    for weather in weathers:
        if weather[0]['id'] > 700:
            return True
    return False


api_key = config('WEATHER_API_KEY')
parameter = {'lat': 26.820553,
             'lon': 30.802498,
             'exclude': "current,minutely,daily",
             'appid': api_key

             }
response = requests.get(
    url="https://api.openweathermap.org/data/2.5/onecall",
    params=parameter)

response.raise_for_status()
data = response.json()

if bring_umberalla(data):

    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today \n bring an umberalla ",
        from_=config("FROM"),
        to=config("TO")
    )
    if message.status=="queued":
        print("Process Completed 100%")

