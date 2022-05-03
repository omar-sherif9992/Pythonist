from bs4 import BeautifulSoup
import pandas, lxml, requests

movies = []
years = []
review = []

URL = "https://www.theguardian.com/film/2019/sep/13/100-best-films-movies-of-the-21st-century"
response = requests.get(url=URL)
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")
# print(soup.prettify())

# movie_names=soup.select(selector=".jsx-4245974604")
movie_tags = soup.select(selector="h2")  # soup.find_all(name="h2",class_="sc-AxhUy fxWvvr")
movie_tags = movie_tags[::-1]

movie_links = soup.select(selector="em a")
movie_links = movie_links[::-1]

for link in movie_links:
    review.append(link.get("href"))

for movie in movie_tags:
    name = movie.select(selector="h2 strong")
    if len(name) == 0:
        continue
    movies.append(name[0].string)
    year = str(movie)
    year = year.split("</strong>")[1][2:6]
    years.append(year)

dict = {
    "Year": years,
    "Movie": movies,
    "Review": review
}

data = pandas.DataFrame(dict)
data.to_csv("best_movies_list.csv")
