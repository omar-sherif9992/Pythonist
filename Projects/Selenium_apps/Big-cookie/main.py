from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

URL="https://orteil.dashnet.org/cookieclicker/"
browser=webdriver.Chrome()
browser.get(url=URL)
cookie=browser.find_element_by_id("bigCookie")
user_name = browser.find_element_by_id("bakeryName")
user_name.click()
user_name=browser.find_element_by_id("bakeryNameInput")
for _ in range(0,10):
    user_name.send_keys(Keys.BACKSPACE)
user_name.send_keys(str(input("what is your name: ")))

user_name.send_keys(Keys.ENTER)




timeout = time.time() + 60*5  # 5 minutes from now
every_5_sec=time.time()+5
while True:
    cookie.click()
    products=browser.find_elements_by_css_selector(".unlocked")
    #it checks on the store every 5 seconds
    if time.time()>every_5_sec:
        for i in range(len(products)-1,-1,-1):
            products[i].click()
        every_5_sec+=5

    if time.time() > timeout :
        break



browser.close()