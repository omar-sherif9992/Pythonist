import time

import requests,smtplib
from datetime import datetime
from decouple import config

MY_LAT = 26.820553  # Your latitude
MY_LONG = 30.802498  # Your longitude


def overhead():
    response = requests.get(url="https://api.wheretheiss.at/v1/satellites/25544")

    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["latitude"])
    iss_longitude = float(data["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    return False


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
    time_now = datetime.now()
    if time_now.hour>=sunset or time_now.hour<=sunrise:
        return True
    return False

while True:
    if overhead() and is_night():
        my_email = str(input("Please enter your email : "))  # the part after the @ is the identity of my email provider
        my_password = str(input("Please enter your Password : "))

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # location of our email provider
                connection.starttls()  # to secure the email
                connection.login(user=my_email, password=my_password)  # login to your email
                connection.sendmail(from_addr=my_email,
                                    to_addrs=config("ADDRS"), #Reciever Address
                                    msg=f"Subject:ISS is over You !\n\n Look Up!!")  # sending the email

        break
    time.sleep(60)
print("Process Completed 100%")

# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
