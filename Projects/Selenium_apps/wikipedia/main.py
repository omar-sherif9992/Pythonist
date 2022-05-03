import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
URL="https://en.wikipedia.org/wiki/Main_Page"
browser = webdriver.Chrome()#with different computer setup you have to pass the file path of the chrome driver
browser.get(url=URL)
# article_count=browser.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
# print(article_count.text)
# article_count.click()#it clicks in to the link

# all_portals=browser.find_element_by_link_text("All portals")#it finds the text thats in between the anchor tag
# all_portals.click()
search_bar=browser.find_element_by_name("search")
search_bar.send_keys("Python")#it will type here the word python in the search bar
search_bar.send_keys(Keys.ENTER)#it presses the key Enter in the keyboard
browser.close()