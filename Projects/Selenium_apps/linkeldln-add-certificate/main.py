from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from decouple import config
from time import sleep


URL = "https://www.linkedin.com/in/omar-sherif-2152021a3/"
EMAIL = config("LINKELDN_EMAIL")
PASSWORD = config("LINKELDN_PASSWORD")
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url=URL)
sleep(3)
sign_in = browser.find_elements_by_css_selector("p button")[1]
sign_in.click()
email_entry = browser.find_element_by_name("session_key")
email_entry.send_keys(EMAIL)
password_entry = browser.find_element_by_name("session_password")
password_entry.send_keys(PASSWORD)
password_entry.send_keys(Keys.ENTER)
sleep(2)
certificate = browser.find_element_by_class_name("add-certification")
certificate.click()
boxs = browser.find_elements_by_css_selector("div input")

for box in boxs:
    box.send_keys("omar ")
    sleep(4)
