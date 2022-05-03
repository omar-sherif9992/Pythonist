# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from Projects.Notification.notification_manager import NotificationManager
from datetime import datetime, timedelta
from data_manager import DataManager
from decouple import config
from flight_search import FlightSearch
from email_manager import EmailManager

NotificationManager().send_sms("mmmm")

# ------------------CONSTANTS-------------------------------------#
ORIGIN_CITY_IATA = "CAI"
FLIGHT_DEALS_SHEETY_ENDPOINT = config("FLIGHT_DEALS_SHEETY_ENDPOINT")
FLIGHT_DEALS_SHEETY_BEARER = config("FLIGHT_DEALS_SHEETY_BEARER")
bearer_headers = {
    "Authorization": f"Bearer {config('FLIGHT_DEALS_SHEETY_BEARER')}"
}
DATE_FROM = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
DATE_TO = (datetime.now() + timedelta(days=6 * 30)).strftime("%d/%m/%Y")

data_manger = DataManager()


# ------------IATA CODE -------------#
def update_codes():
    """intializes the Iata code of each country """
    for data in data_manger.sheet_data:
        flight_search_code = FlightSearch().get_destination_code(data['city'])
        data_manger.update_codes(code=flight_search_code, id=data['id'])
    data_manger.get_data()


# update_codes()


def flights():
    for destination in data_manger.sheet_data:
        if ORIGIN_CITY_IATA == destination['iataCode']:
            continue
        flight = FlightSearch().check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=DATE_FROM,
            to_time=DATE_TO
        )
        if flight is None:
            data_manger.update_price(-1, destination['id'])
            continue

        if flight.price < destination["lowestPrice"] or destination['lowestPrice']<0:
            data_manger.update_price(flight.price, destination['id'])
            message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
            NotificationManager().send_sms(message)
            EmailManager().send_email(message)



