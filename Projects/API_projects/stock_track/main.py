import requests, os
from datetime import datetime
from twilio.rest import Client
from decouple import config

account_sid = config("ACCOUNT_SID")  # Copied from my Dashboard
auth_token = config("AUTH_TOKEN")  # Copied from my Dashboard

UP = "🔺"
DOWN = "🔻"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_parameters = {"function": "TIME_SERIES_DAILY",
                    "symbol": STOCK_NAME,
                    "apikey": config("STOCK_API_KEY")
                    }

time_now = datetime.now()
today = str(time_now.date())
today_date = today.split("-")
today_date[2] = str(int(today_date[2]) - 1)
yesterday_date = today_date
before_yesterday_date = [t for t in today_date]
before_yesterday_date[2] = str(int(yesterday_date[2]) - 1)
before_yesterday_date = "-".join(before_yesterday_date)
yesterday_date = "-".join(yesterday_date)
news_parameters = {'apiKey': config("NEWS_API_KEY"),
                   'language': 'en',
                   'from': before_yesterday_date,
                   'to': yesterday_date,
                   'qInTitle': COMPANY_NAME,

                   }


def percentage() -> float:
    stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
    stock_response.raise_for_status()
    stock_data = stock_response.json()
    time_series = stock_data['Time Series (Daily)']
    stock_yesterday = time_series[yesterday_date]
    stock_before_yesterday = time_series[before_yesterday_date]
    difference = (float(stock_yesterday['4. close']) - float(stock_before_yesterday['4. close']))
    percentage_difference = (difference / float(stock_yesterday['4. close'])) * 100
    return percentage_difference


def send_sms(message: str, percentage: float):
    if percentage>0:
        message=f"\n{COMPANY_NAME} : {UP} {round(percentage)}%\n"+message
    else:
        message=f"{COMPANY_NAME} : {DOWN} {round(percentage)}%\n"+message


    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=message,
        from_=config("FROM"),# write down your twilo verified sender number  as a string without config
        to=config("TO")# write down your twilo verified reciever number  as a string without config
    )
    print("Process Completed 100%")

# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# {COMPANY_NAME} : 🔺{percentage}%
def get_news() -> []:
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    data = news_response.json()
    articles = data['articles']
    if len(articles)==0:
        return None
    articles = articles[:3]
    messages = [f"Headline :{article['title']} \n Brief :{article['description']}  " for article in articles]
    return messages


per = percentage()

messages = get_news()
print(messages)
if messages ==None:
    for message in messages:
        print(message)
        send_sms(message, per)

