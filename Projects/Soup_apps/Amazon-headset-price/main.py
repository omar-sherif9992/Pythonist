# ---------------------------------------------Imports-----------------------------------------------------------#
import requests, pandas, lxml
from Projects.Notification.email_manager import EmailManager
from bs4 import BeautifulSoup
from Projects.Soup_apps.Web_Scrape.Soup import create_soup

# ---------------------------------------------Constants-----------------------------------------------------------#
# use the product url that you want
URL = "https://www.amazon.com/Hori-PlayStation-Surround-Gaming-Neckset-5/dp/B097VG9PP9/ref=sr_1_7?crid=2PHHEZ7OA7LPR&dchild=1&keywords=playstation+5&qid=1629463174&sprefix=plays%2Caps%2C742&sr=8-7"
# use http://myhttpheader.com/ to change the headers it is according to your computer
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Accept-Language": "en-GB,en;q=0.9,de-DE;q=0.8,de;q=0.7,ar-EG;q=0.6,ar;q=0.5,en-US;q=0.4"
}
# ---------------------------------------------main-----------------------------------------------------------#
soup = create_soup(url=URL, headers=headers)
price = float((str((soup.select_one(selector="#priceblock_ourprice")).string))[1:])
shipping_price = soup.find_all(name="span", class_="a-color-secondary")[3].string

title = str(soup.find("title").string).split(":")[1]

if price < 90:
    EmailManager().send_email(title=title, to_addrs="Omar.sherif9992@gmail.com",
                              message=f"Your Favorite Product is on Sale\n\nprice: ${price}\n\nShipping: {shipping_price}",
                              first_name="Omar", last_name="Sherif")
