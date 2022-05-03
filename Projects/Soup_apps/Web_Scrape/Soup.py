import requests,lxml
from bs4 import BeautifulSoup


def create_soup(url:str,**kwargs)->BeautifulSoup:
        try:
                 response=requests.get(url=url,headers=kwargs['headers'])

                 response.raise_for_status()
        except:
                response = requests.get(url=url)
        webpage=response.text
        soup=BeautifulSoup(webpage,"lxml")
        return soup