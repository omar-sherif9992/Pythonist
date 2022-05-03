import requests
from decouple import config
from datetime import datetime

# API_DOCUMENTATION="https://docs.pixe.la/"
# the graph https://pixe.la/v1/users/omar-sherif9992/graphs/graph2.html
#TODO:make a Pixela app using  tkinter and pandas

MY_ACCOUNT_PIXELA_ENDPOINT = config("MY_ACCOUNT_PIXELA_ENDPOINT")
MY_GRAPH_PIXELA_ENDPOINT = config("MY_GRAPH_PIXELA_ENDPOINT")
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = config('PIXELA_TOKEN')
USERNAME = config("PIXELA_USERNAME")

#My Graph prefered configuration
PIXELA_ID = 1
PIXELA_NAME = "Weight Loss Graph"
PIXELA_UNIT = "Kg"
PIXELA_TYPE = "float"
PIXELA_COLOR = "shibafu"
TODAY = datetime.now()
TODAY = TODAY.strftime("%Y%m%d")  # https://www.w3schools.com/python/python_datetime.asp
print(f"Today : { TODAY}")

headers = {
    "X-USER-TOKEN": TOKEN
}


def create_user():
    pixela_json = {
        'token': TOKEN,
        'username': USERNAME,
        'agreeTermsOfService': "yes",
        'notMinor': "yes"
    }
    response = requests.post(url=PIXELA_ENDPOINT, json=pixela_json)
    print(response.text)  # sucesss message


# create_user(token,username) #give your own info and reformat file

def open_graph():
    response = requests.get(url=MY_ACCOUNT_PIXELA_ENDPOINT)
    data = response.text
    with open("MY_Graph.htm", 'w') as file:
        file.write(data)
        print(data)  # sucesss message


def create_graph(id: int, name: str, unit: str, type: str, color: str):
    """Creating a new graph that is unique by its id"""
    PIXELA_ID = f"graph{id}"  # [required] It is an ID for identifying the pixelation graph.Validation rule: ^[a-z][a-z0-9-]{1,16}
    PIXELA_NAME = f"{name} Graph"  # [required] It is the name of the pixelation graph.
    PIXELA_UNIT = unit  # [required] It is a unit of the quantity recorded in the pixelation graph. Ex. commit, kilogram, calory.
    PIXELA_TYPE = type  # [required] It is the type of quantity to be handled in the graph. Only int or float are supported. #
    PIXELA_COLOR = color  # [required] Defines the display color of the pixel in the pixelation graph.shibafu (green), momiji (red), sora (blue), ichou (yellow), ajisai (purple) and kuro (black) are supported as color kind.

    graph_config = {
        'id': PIXELA_ID,
        "name": PIXELA_NAME,
        "unit": PIXELA_UNIT,
        "type": PIXELA_TYPE,
        "color": PIXELA_COLOR,
        "timezone": "Africa/Cairo"
    }
    response = requests.post(url=MY_GRAPH_PIXELA_ENDPOINT, json=graph_config, headers=headers)
    print(response.text)



def create_pixel(date: str, quantity: str):
    THIS_GRAPH_PIXELA_ENDPOINT = f"{MY_GRAPH_PIXELA_ENDPOINT}/graph{PIXELA_ID}"
    pixela_params = {
        "date": date,
        "quantity": quantity,

    }
    response = requests.post(url=THIS_GRAPH_PIXELA_ENDPOINT, json=pixela_params, headers=headers)
    print(response.text)


def update_graph_timeZone():
    THIS_GRAPH_PIXELA_ENDPOINT = f"{MY_GRAPH_PIXELA_ENDPOINT}/graph{PIXELA_ID}"
    pixela_params = {
        "timezone": "Africa/Cairo"
    }
    response = requests.put(url=THIS_GRAPH_PIXELA_ENDPOINT, json=pixela_params, headers=headers)
    print(response.text)


def update_pixel(date: str, quantity: str):
    THIS_GRAPH_PIXELA_ENDPOINT = f"{MY_GRAPH_PIXELA_ENDPOINT}/graph{PIXELA_ID}/{date}"
    pixela_params = {
        "quantity": quantity
    }
    response = requests.put(url=THIS_GRAPH_PIXELA_ENDPOINT, json=pixela_params, headers=headers)
    print(response.text)

def delete_graph(id:str):
    """for deleteing the graph"""
    THIS_GRAPH_PIXELA_ENDPOINT = f"{MY_GRAPH_PIXELA_ENDPOINT}/graph{id}"
    response=requests.delete(url=THIS_GRAPH_PIXELA_ENDPOINT,headers=headers)
    print(response.text)

def delete_pixel(id:str,date:str):
    """deletes a pixel from the graph"""
    THIS_GRAPH_PIXELA_ENDPOINT = f"{MY_GRAPH_PIXELA_ENDPOINT}/graph{PIXELA_ID}/{date}"
    response=requests.delete(url=THIS_GRAPH_PIXELA_ENDPOINT,headers=headers)
    print(response.text)


#update_graph_timeZone() --># for updating the graph timezone

#delete_graph("graphPIXELA_ID") #for deleteing the graph
#create_graph(PIXELA_ID,PIXELA_NAME,PIXELA_UNIT,PIXELA_TYPE,PIXELA_COLOR) -->Creating a graph
#create_pixel(TODAY,str(input("Enter how much you loosed weight Today:")))
#update_pixel(TODAY,str(input("Enter how much you loosed weight Today:")))
#delete_pixel("PIXELA_ID",TODAY) -->#deletes a pixel from the graph
open_graph()