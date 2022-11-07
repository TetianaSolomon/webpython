import threading
from datetime import datetime
import time
import socket
from sys import getsizeof

def handle(clientsocket):
    while True:
        try:
            message = clientsocket.recv(1024).decode(format)
            if message == "Exit":
                clientsocket.close()
                break
            print(f'{datetime.now().strftime("%H:%M:%S")} {message}')
            time.sleep(5)
            size = clientsocket.send(message.encode(format))
            if size != len(message.encode(format)):
                print("Problem with sending data")
        except:
            print("Disconnected with client")
            break

def get():
    while True:
        clientsocket, adress = serversocket.accept()
        thread = threading.Thread(target=handle, args=(clientsocket,))
        thread.start()


host = "127.0.0.1"
port = 10000
format = 'utf-8'

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((host, port))
serversocket.listen()

print("Server started")
get()