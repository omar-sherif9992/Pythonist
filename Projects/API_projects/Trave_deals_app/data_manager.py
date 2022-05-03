from pprint import pprint
import requests
from decouple import config

FLIGHT_DEALS_SHEETY_ENDPOINT = config("FLIGHT_DEALS_SHEETY_ENDPOINT")
FLIGHT_DEALS_SHEETY_BEARER = config("FLIGHT_DEALS_SHEETY_BEARER")
bearer_headers = {
    "Authorization": f"Bearer {config('FLIGHT_DEALS_SHEETY_BEARER')}"
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_data = []
        self.get_data()

    def get_data(self):
        """returns the google data sheet in JSON"""
        response = requests.get(url=FLIGHT_DEALS_SHEETY_ENDPOINT)
        response.raise_for_status()
        self.sheet_data = response.json()['prices']
        response.raise_for_status()
        return response.json()['prices']

    def get_prices_column(self):
        data = self.get_data()
        prices = []
        for row in data:
            prices.append(row['lowestPrice'])

        pprint(prices)
        return prices

    def get_cities_column(self):
        data = self.get_data()
        cities = []
        for row in data:
            cities.append(row['city'])

        pprint(cities)
        return cities

    def missing_code(self):
        data = self.sheet_data
        for row in data:
            if len(row['iataCode']) == 0:
                return True
        return False

    def update_codes(self, code, id):
        if self.missing_code():
            new_data = {
                "price": {
                    "iataCode": code
                }
            }
            response = requests.put(url=f"{FLIGHT_DEALS_SHEETY_ENDPOINT}/{id}", json=new_data)
            response.raise_for_status()


    def update_price(self, price, id):
        new_data = {
            "price": {
                "lowestPrice": price
            }
        }
        response = requests.put(url=f"{FLIGHT_DEALS_SHEETY_ENDPOINT}/{id}", json=new_data)
        response.raise_for_status()
# data = DataManager()
# data.update_codes()
# data.get_data()
