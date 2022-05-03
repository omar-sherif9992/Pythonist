from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from time import sleep
from alive_progress import alive_bar

def keyword_grabber():
    total=5
    keyword = str(input("Please enter your keyword:"))
    with alive_bar(total,bar='filling',title='Searching for related keywords') as bar:
        URL="https://keywordshitter.com/"
        op = webdriver.ChromeOptions()
        op.add_argument('headless')
        browser = webdriver.Chrome(options=op)
        browser.get(url=URL)
        text_input=browser.find_element_by_css_selector('.bigwide')
        bar()
        sleep(1)
        text_input.send_keys(keyword)
        start_button=browser.find_element_by_css_selector('.bigger-button')
        bar()
        sleep(2)
        start_button.send_keys(Keys.ENTER)
        bar()
        sleep(6)
        bar()
        sleep(6)
        all_keywords=str(text_input.get_attribute('value')).splitlines()
        all_keywords=(',').join(all_keywords)
        if "'" in all_keywords:
           all_keywords= all_keywords.replace("'","")
        if '"' in all_keywords:
            all_keywords=all_keywords.replace('"', "")
        bar()


        browser.close()
    print(all_keywords)




if __name__=="__main__":
    keyword_grabber()