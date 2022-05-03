from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from decouple import config
from time import sleep

URL = "https://tinder.com/app/recs"
EMAIL = config("FACEBOOK_EMAIL")
PASSWORD = config("FACEBOOK_PASSWORD")
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url=URL)

log_in = browser.find_element_by_css_selector(
    "#u-648818393 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div > div > header > div > div:nth-child(2) > div.H\(40px\).Px\(28px\) > a")
log_in.click()
sleep(2)
facebook = browser.find_element_by_css_selector(
    "#u1917767827 > div > div > div.Ta\(c\).H\(100\%\).D\(f\).Fxd\(c\).Pos\(r\) > div > div:nth-child(4) > span > div:nth-child(2) > button")
facebook.click()
sleep(2)
pprint(browser.window_handles)
facebook_page = browser.window_handles[1]
browser.switch_to.window(facebook_page)
print(f"logging in by {browser.title}")
facebook_email = browser.find_element_by_name("email")
facebook_email.send_keys(EMAIL)
facebook_password = browser.find_element_by_name("pass")
facebook_password.send_keys(PASSWORD)
facebook_password.send_keys(Keys.ENTER)
sleep(2)
tinder_page = browser.window_handles[0]
browser.switch_to.window(tinder_page)
print(f"Successfully Logged in {browser.title}")
sleep(4)
location_allow = browser.find_element_by_xpath('//*[@id="u1917767827"]/div/div/div/div/div[3]/button[1]')
location_allow.click()
sleep(2)
notifications_allow = browser.find_element_by_xpath('//*[@id="u1917767827"]/div/div/div/div/div[3]/button[2]')
notifications_allow.click()
print("location is setuped ")
sleep(4)
buttons=browser.find_elements_by_css_selector("div button")
like_button=None
for button in buttons:
    if str(button.text)=="LIKE":
        like_button=button
for _ in range(0,100):
    try:
        like_button.click()

        # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = browser.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            print("Match !Try again")
    except NoSuchElementException:
        print("Try again")