from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import StaleElementReferenceException
from decouple import config
from time import sleep
from instagram_login import InstagramLogin

INSTAGRAM_EMAIL=config("INSTAGRAM_EMAIL")
INSTAGRAM_PASSWORD=config("INSTAGRAM_PASSWORD")
SIMILAR_USER="motivationacts"
URL=f"https://www.instagram.com/{SIMILAR_USER}/"
instagram=InstagramLogin()
instagram.login(url=URL,email=INSTAGRAM_EMAIL,password=INSTAGRAM_PASSWORD)
instagram.followers_page()
instagram.follow(SIMILAR_USER)
