from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import StaleElementReferenceException
from decouple import config
from time import sleep

class InstagramLogin:
    def __init__(self):
        self.browser=webdriver.Chrome()
        self.browser.maximize_window()
    def follow(self,user:str):
        follow_buttons=self.browser.find_elements_by_css_selector("li button")
        # scroll=self.browser.find_element_by_class_name("isgrP")
        for follow_button in follow_buttons:
            print(follow_button.text)
            if str(follow_button.text) == "Follow":
                follow_button.click()
                sleep(1)
            # scroll.send_keys(Keys.ARROW_DOWN)
        print(f"Followed all the the Followers of {user}")
    def followers_page(self):
        followers_pg=self.browser.find_element_by_css_selector("li a")
        followers_pg.click()
        sleep(4)


    def login(self,url:str,email:str,password:str):
        self.browser.get(url)
        sleep(2)
        log_in=self.browser.find_element_by_class_name("L3NKy")
        log_in.click()
        sleep(2)
        username_entry=self.browser.find_element_by_name("username")
        username_entry.send_keys(email)
        password_entry=self.browser.find_element_by_name("password")
        password_entry.send_keys(password)
        password_entry.send_keys(Keys.ENTER)
        sleep(3)
        not_now=self.browser.find_element_by_css_selector("main div div button")
        not_now.click()
        sleep(4)
        print("Successfully Logged in")


