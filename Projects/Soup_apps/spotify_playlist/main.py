from bs4 import BeautifulSoup
import pandas, requests, lxml
from spotify import create_playlist
#https://www.billboard.com/charts/hot-100/2002-07-20

while True:
    try:
        year=str(input('Enter the Year YYYY : '))
        URL = f"https://www.billboard.com/charts/hot-100/{year}-{str(input('Enter the Month MM : '))}-{str(input('Enter the Day DD: '))}"
        response = requests.get(url=URL)
        response.raise_for_status()
        webpage = response.text
        soup = BeautifulSoup(webpage, "html.parser")
        break
    except :
        print("Invalid Date please enter it in the right format YYYY-MM-DD")




# print(soup.prettify())
songs=soup.find_all(name="span",class_="chart-element__information__song text--truncate color--primary")#soup.select(selector="button span span")
playlist=[]
years=[]
for song in songs:
    playlist.append(song.string)
    years.append(year)

song_dict={"Songs":playlist,
           "Year":years

           }
data=pandas.DataFrame(song_dict)
data.to_csv(f"Top-100-songs-in-{year}.csv ")
create_playlist(playlist,year)
