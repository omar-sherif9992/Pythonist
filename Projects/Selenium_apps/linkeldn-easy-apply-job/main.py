from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from decouple import config
from time import sleep

#-----------------------------------------------------------------     CONSTANTS   -----------------------------------------------------------#
LINKELDN_EMAIL = config("LINKELDN_EMAIL")
LINKELDN_PASSWORD = config("LINKELDN_PASSWORD")
PHONE = config("PHONE_NUMBER")
URL = "https://www.linkedin.com/jobs/search/?f_AL=true&f_E=1&f_JT=I&f_TPR=r2592000&f_WRA=true&geoId=92000001&keywords=python&location=Remote"

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url=URL)
sign_in = browser.find_element_by_link_text("Sign in")
sign_in.click()
email = browser.find_element_by_name("session_key")
email.send_keys(LINKELDN_EMAIL)
password = browser.find_element_by_name("session_password")
password.send_keys(LINKELDN_PASSWORD)
password.send_keys(Keys.ENTER)
sleep(2)
jobs = browser.find_elements_by_css_selector(".job-card-container--clickable")
applied = None
print(len(jobs))
new_applied = {}
i = 0
for job in jobs:
    try:
        if job is None or str(job.text) == "Try Premium for free" or str(job.text) == "":
            print("enter")
            continue
        company_name = str(job.text).split("\n")[0]
        company_link = job.find_element_by_css_selector("a").get_attribute("href")
        job.click()
        sleep(1)
        apply = browser.find_element_by_css_selector(".jobs-apply-button--top-card button")
        apply.click()

        sleep(2)
        next_button = browser.find_element_by_css_selector("footer button")

        if next_button.get_attribute("data-control-name") == "continue_unify":
            close_apply = browser.find_element_by_css_selector(".artdeco-modal__dismiss")
            close_apply.click()
            sleep(2)
            discard = browser.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard.click()
            sleep(4)
            print(f"{company_name} is disregarded \n\n")
            continue
        else:
            phone = browser.find_element_by_css_selector(".fb-single-line-text input")
            if str(phone.text) != str(PHONE):
                print(phone.text)
                for _ in range(0, 10):
                    phone.send_keys(Keys.BACKSPACE)
                phone.send_keys(PHONE)
            sleep(1)
            next_button.click()
            print(f"Company:{company_name} is applied \n Company Link:{company_link} \n\n ")
            i += 1
            new_applied[i] = {"Company-Name": company_name,
                              "Company-Link": company_link}
            # TODO recheck needed
            # Once application completed, close the pop-up window.
            sleep(4)
            close_button = browser.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
    except NoSuchElementException as message:
        try:
            applied = browser.find_element_by_css_selector(".artdeco-inline-feedback__message")
            if applied is not None:
                print(f"{company_name} already {applied.text}\n\n")
        except NoSuchElementException:
            pass
        sleep(4)
        applied = None
        continue
    except ElementNotInteractableException as message:
        print(message)
        sleep(4)
    sleep(4)

pprint(new_applied)
browser.quit()

# https://www.linkedin.com/jobs/view/2692526997/?eBP=JOB_SEARCH_ORGANIC&recommendedFlavor=JOB_SEEKER_QUALIFIED&refId=0MQL%2FpL6e9C2mrchF2kfKA%3D%3D&trackingId=CsLxjs6ZkETCkDF9EeifbQ%3D%3D&trk=flagship3_search_srp_jobs
