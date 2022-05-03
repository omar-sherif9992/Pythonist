from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import StaleElementReferenceException
from decouple import config
from time import sleep
from bs4 import BeautifulSoup
from Projects.Soup_apps.Web_Scrape.Soup import create_soup
import pandas

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Accept-Language": "en-GB,en;q=0.9,de-DE;q=0.8,de;q=0.7,ar-EG;q=0.6,ar;q=0.5,en-US;q=0.4"
}

ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.81029738378906%2C%22east%22%3A-122.05636061621094%2C%22south%22%3A37.55406737907953%2C%22north%22%3A37.99585553467577%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A823461%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A2000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
FORM_URL = "https://forms.gle/yV6nQCsjEVsEZLHz7"
soup = create_soup(ZILLOW_URL, headers=headers)
ads = soup.find_all(name="div", class_="list-card-price")
prices=[]
locations=[]
links=[]
for ad in ads:
    prices.append(ad.string)

ads = soup.find_all(name="a", class_="list-card-link")
for ad in ads:
    if ad.get("href") == None or ad.string == None:
        continue

    if "https://www.zillow.com" in ad.get("href"):
        links.append(ad.get("href"))
    else:
        links.append(f"https://www.zillow.com{ad.get('href')}")
    locations.append(ad.string)

print("Data is forwarded to the Goggle form\n ")


browser=webdriver.Chrome()
for i in range(0,len(prices)):
    if prices[i] ==None:
        continue
    browser.get(FORM_URL)
    browser.maximize_window()
    sleep(2)
    editors = browser.find_elements_by_class_name("exportInput")


    editors[0].send_keys(locations[i])
    editors[1].send_keys(links[i])
    editors[2].send_keys(prices[i])
    send_button=browser.find_element_by_class_name("freebirdFormviewerViewNavigationSubmitButton")
    send_button.click()
    sleep(1)

print("Successfull filled the form ")
browser.quit()
#Spread sheet link
# https://docs.google.com/spreadsheets/d/1ypH9bJA_OS-44u3CaC4lZmOFQIDOw-FoPtVu6mUeCqI/edit?resourcekey#gid=1813545332