import requests
from bs4 import BeautifulSoup
import lxml

response = requests.get(
    url="https://news.ycombinator.com")  # the request allows us to get the html text because the url is not an api url

soup = BeautifulSoup(response.text, "lxml")
# print(soup.prettify())
articles = soup.find_all(name="a", class_="storylink")  # or soup.select(selector="a .storylink")
upvotes=soup.find_all(name="span",class_="score")
upvotes_text=[int(a.string.split(" ")[0]) for a in upvotes]
article_text=[]
article_href=[]
for a in articles:
    article_text.append(a.string)
    article_href.append(a.get("href"))
max=upvotes_text[0]
for i in range(1,len(upvotes_text)):
    if max <upvotes_text[i]:
        max=upvotes_text[i]
index=upvotes_text.index(max)
print(f"{index+1}. The Highest upvotes :\n Article : {article_text[index]}\n upvotes : {upvotes_text[index]} \n {article_href[index]}")


    # print(f" {i+1}. {articles[i].string}\n{articles[i].get('href')}\n\n")

