import requests, os, pandas
from decouple import config
from datetime import datetime





# API Docs https://trackapi.nutritionix.com/docs/#/default/post_v2_auth_signup

# Google Sheet that has been Used: https://docs.google.com/spreadsheets/d/1enkLYbbGa8hfEEfrtygG0uYfyZMq3pWF9QU-ZVOT__g/edit#gid=0

# Sheety API : https://sheety.co/
bearer_headers = {
    "Authorization": f"Bearer {config('WORKOUT_TRACK_SHEETY_BEARER')}"
}

NUTRITIONIX_API_ID = config("NUTRITIONIX_API_ID")
NUTRITIONIX_API_KEY = config("NUTRITIONIX_API_KEY")
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
WORKOUT_TRACK_SHEETY_ENDPOINT = config("WORKOUT_TRACK_SHEETY_ENDPOINT")
GENDER = config("GENDER")
WEIGHT_KG = config("WEIGHT_KG")
HEIGHT_CM = config("HEIGHT_CM")
AGE = config("AGE")

USER = {
    "password": "string",
    "email": "string",
    "first_name": "string",
    "timezone": "string",
    "ref": "string"
}
headers = {"x-app-id": NUTRITIONIX_API_ID,
           "x-app-key": NUTRITIONIX_API_KEY}


def today_date() -> str:
    today = datetime.now()
    today = today.strftime("%Y/%m/%d")
    return today


def current_time() -> str:
    today = datetime.now()
    today = today.strftime("%H:%M:%S")
    return today


def calories_lost(query: str, gender: str, weight_kg: str, height_cm: str, age: str):
    if "minutes" not in query:
        query += " minutes"

    parameters = {"query": query,
                  "gender": gender,
                  "weight_kg": weight_kg,
                  "height_cm": height_cm,
                  "age": age
                  }

    response = requests.post(url=NUTRITIONIX_ENDPOINT, headers=headers, json=parameters)
    response.raise_for_status()
    return response.json()


def add_row(exercise: str, duration: str, calories: str):
    """Dont use this to add a Row"""
    params = {"sheet1": {
        "date": today_date(),
        "time": current_time(),
        "exercise": exercise,
        "duration": duration,
        "calories": calories

    }}
    headers = {"Content-Type": "application/json"}
    headers.update(bearer_headers)
    response = requests.post(url=WORKOUT_TRACK_SHEETY_ENDPOINT, json=params, headers=headers)
    if response.raise_for_status() is None:
        print("Successfully row is added 100%")
        update_csv()


def added_google_sheet_row():
    """Adds a row in the google sheet"""
    exercise_dict = calories_lost(str(input("Enter Your workout : ")) +" for " +str(input("Enter Duration : ")), GENDER,
                                  WEIGHT_KG,
                                  HEIGHT_CM, AGE)
    for exercise_dict in  exercise_dict["exercises"]:
        add_row(exercise=(str(exercise_dict["user_input"])).title(),
                duration=(str(exercise_dict["duration_min"])).title(), calories=exercise_dict["nf_calories"])


def delete_row(row_number: str):
    """Delete row from Google Data Sheet"""
    WORKOUT_TRACK_SHEETY_DELETE_ENDPOINT = f"{WORKOUT_TRACK_SHEETY_ENDPOINT}/{row_number}"
    response = requests.delete(url=WORKOUT_TRACK_SHEETY_DELETE_ENDPOINT,headers=bearer_headers)
    if response.raise_for_status() is None:
        print("Successfully row is Deleted 100%")
        update_csv()


def get_data():
    response = requests.get(url=WORKOUT_TRACK_SHEETY_ENDPOINT, headers=bearer_headers)
    print(response.json())
    return response.json()


def turn_csv(sheets):
    """turns the google datasheet to csv but needs """
    dates = []
    times = []
    exercises = []
    durations = []
    calories = []

    for sheet in sheets:
        dates.append(sheet['date'])
        times.append(sheet['time'])
        exercises.append(sheet['exercise'])
        durations.append(sheet['duration'])
        calories.append(sheet['calories'])

    data = {
        'Date': dates,
        'Time': times,
        "Exercises": exercises,
        'durations (mins)': durations,
        'calories': calories
    }
    df = pandas.DataFrame(data)
    df.to_csv("Workout tracking.csv")
    print("Successfully converted Google Data Sheet into Excel Sheet")


# added_google_sheet()

def update_csv():
    "Update csv file"
    turn_csv(get_data()['sheet1'])  # turns the google datasheet to csv


added_google_sheet_row()
