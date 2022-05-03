from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from decouple import config
from time import sleep
from Internet_Speed_TwitterBot import InternetSpeedTwitterBot

SPEED_Url="https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/home"
TWITTER_EMAIL = config("TWITTER_EMAIL")
TWITTER_PASSWORD = config("TWITTER_PASSWORD")
TWITTER_USERNAME = config("TWITTER_USERNAME")
speed=InternetSpeedTwitterBot()
speed.get_internet_speed(url=SPEED_Url)
speed.tweet_at_provider(url=TWITTER_URL,email=TWITTER_EMAIL,password=TWITTER_PASSWORD,username=TWITTER_USERNAME)




