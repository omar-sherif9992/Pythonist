import requests
from datetime import datetime

dict = {'lat': 26.820553,
        'long': 30.802498
    , 'formatted': 0}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=dict)
response.raise_for_status()
data = response.json()
sunrise = data["results"]['sunrise']
sunset = data["results"]['sunset']

time = datetime.now()

sunrise = sunrise.split("T")
sunrise = sunrise[1].split(":")
sunrise_hour = sunrise[0]
sunset_hour = sunset.split("T")[1].split(":")[0]
time_hour = time.hour

print(time_hour)
print(sunrise_hour)
print(sunset_hour)
