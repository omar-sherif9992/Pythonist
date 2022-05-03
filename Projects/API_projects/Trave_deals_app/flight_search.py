import requests
from pprint import pprint
import requests
from decouple import config
from flight_data import FlightData
import flight_data

KIWI_LOCATIONS_API = config("KIWI_LOCATIONS_API")
KIWI_API_KEY = config("KIWI_API_KEY")
KIWI_SEARCH_KEY = config("KIWI_SEARCH_KEY")
headers = {"apikey": KIWI_API_KEY}


class FlightSearch:

    def get_destination_code(self, city_name):
        # location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=KIWI_LOCATIONS_API, headers=headers, params=query)
        results = response.json()["locations"]
        try:
            code = results[0]["code"]
        except:
            code = None
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time)-> FlightData:
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time,
            "date_to": to_time,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        response = requests.get(url=KIWI_SEARCH_KEY, headers=headers, params=query)
        response.raise_for_status()
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data

