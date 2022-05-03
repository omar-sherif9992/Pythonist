import smtplib
from decouple import config
import requests
from pprint import pprint

FLIGHT_DEALS_DATA_SHEETY_ENDPOINT = config("FLIGHT_DEALS_DATA_SHEETY_ENDPOINT")


class EmailManager:
    def __init__(self):
        self.users = self.get_data()

    def get_data(self):
        response = requests.get(url=FLIGHT_DEALS_DATA_SHEETY_ENDPOINT)
        response.json()
        pprint(response.json()["data"])
        return response.json()["data"]

    def send_email(self, message):
        my_email = config("MY_EMAIL")  # the part after the @ is the identity of my email provider
        my_password = config("MY_PASSWORD")

        for user in self.users:
            print(user['email'])
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                # location of our email provider
                connection.starttls()  # to secure the email
                connection.login(user=my_email, password=my_password)  # login to your email
                connection.sendmail(from_addr=my_email,
                                    to_addrs=user['email'],
                                    msg=f"Subject:Flight Deals\n\nDear{user['firstName']} {user['lastName']},\n\n {message}.")  # sending the email

    def contains(self, email: str):
        email=email.lower()
        for user in self.users:
            if (str (user['email'])).lower() == email.lower():
                return True
        return False

    def add_email(self, first_name, last_name, email:str):
        if not self.contains(email=str(email)):
            parameters = {
                "datum": {
                    'email': email,
                    'firstName': first_name,
                    'lastName': last_name
                }
            }

            response = requests.post(url=FLIGHT_DEALS_DATA_SHEETY_ENDPOINT, json=parameters)
            response.raise_for_status()
            print("You've Joined the Club")
            self.users.append(response.json()['datum'])
            return True
        else:
            return False
