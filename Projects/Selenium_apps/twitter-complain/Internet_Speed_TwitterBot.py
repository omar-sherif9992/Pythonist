from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

PROMISED_DOWN = 3
PROMISED_UP = 0.5


class InternetSpeedTwitterBot:
    def __init__(self):
        self.down = 0.0
        self.up = 0.0
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()

    def get_internet_speed(self, url):
        self.browser.get(url=url)
        print("Connecting to the Internet")
        sleep(6)
        go_button = self.browser.find_element_by_css_selector(".start-button a")
        go_button.click()
        print("Loading Data....")
        sleep(60)
        self.down = float(self.browser.find_element_by_css_selector(".download-speed").text)
        print(f"Your Download Speed : {self.down} Mbps")
        self.up = float(self.browser.find_element_by_css_selector(".upload-speed").text)
        print(f"Your Upload Speed : {self.up} Mbps")

    def tweet_at_provider(self, url: str, email: str, password: str, username: str):
        if PROMISED_DOWN<self.down or PROMISED_UP<self.up:
            print("Good we got no Problems wih the Internet ")
            return
        sleep(2)
        self.browser.get(url)
        sleep(2)
        email_entry = self.browser.find_element_by_name("session[username_or_email]")
        email_entry.send_keys(email)
        password_entry = self.browser.find_element_by_name("session[password]")
        password_entry.send_keys(password)
        password_entry.send_keys(Keys.ENTER)
        sleep(4)
        if str(self.browser.title) == "Login on Twitter / Twitter":
            print("Re-trying to login with Username instead of Email !")
            email_entry = self.browser.find_element_by_name("session[username_or_email]")
            email_entry.send_keys(username)
            password_entry = self.browser.find_element_by_name("session[password]")
            password_entry.send_keys(password)
            password_entry.send_keys(Keys.ENTER)
            sleep(4)

        print("Successfully Logged in")
        text_entry = self.browser.find_element_by_class_name("public-DraftStyleDefault-block")
        text_entry.send_keys(f"Why is my Download speed is {self.down}")
        text_entry.send_keys(Keys.ENTER)
        text_entry.send_keys(f"and Why is my Upload speed is {self.up}")
        text_entry.send_keys(Keys.ENTER)
        text_entry.send_keys(f"I'm So Pissed")
        add = self.browser.find_elements_by_css_selector("div div div")
        add_button = None
        for butoon in add:
            if str(butoon.text) == "Tweet":
                add_button = butoon
        add_button.click()
        print("Successfully Tweeted")
        self.browser.quit()