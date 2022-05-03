from pprint import pprint

import requests
class Products:
    def __init__(self):
        self.url="https://dummyproducts-api.herokuapp.com"
        response=requests.get(url=self.url)
        print(response)
        self.products=response.json()

    def __repr__(self):
        print("Presents all the products")
        pprint(self.products[0])


if __name__=="__main__":
    p=Products()
    pprint(p.products)