import socket
import threading

PORT = 5050
# print(socket.gethostname()) # Prints the user name of the end system device
SERVER = socket.gethostbyname(socket.gethostname())  # gets the ip address from the end system name

ADDR=(SERVER,PORT)
# AF_inet means that is over the internet
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(connection,addr):
    pass

def start():
    server.listen()
    while True:
        connection ,addr=server.accept()
        # thread=threading.Thread(target=handle_client(,args=(c)))

print("Starting Server now ...")
start()