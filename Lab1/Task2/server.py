import socket
import threading
from collections import deque

def send_all(message, current_client=None):
    with open('messages.txt', 'a+') as file:
        file.write(message + '\n')
    for clientsocket in clientssocket:
        if clientsocket != current_client:
            clientsocket.send(message.encode(format))

def log_in(clientsocket):
    while True:
        try:
            if clientsocket not in clientssocket:
                clientsocket.send('start'.encode(format))
                login = clientsocket.recv(1024).decode(format)
                if login not in users:
                    clientsocket.send('registration'.encode(format))
                    password = clientsocket.recv(1024).decode(format)
                    users[login] = password
                    with open('users.txt', 'a') as file:
                        file.write(f"{login} {password}\n")
                else:
                    clientsocket.send('log in'.encode(format))
                    password = clientsocket.recv(1024).decode(format)
                    if users[login] != password:
                        clientsocket.send('Incorrect password'.encode(format))
                        continue
                start_chat(clientsocket, login)
        except:
            continue

def client_handler(clientsocket, login):
    while True:
        try:
            message = clientsocket.recv(1024).decode(format)
            send_all(message, clientsocket) 
        except:
            if clientsocket in clientssocket:
                clientssocket.remove(clientsocket)
                send_all(f"[{login}] Left the chat!")
                print(f"{login} Left the chat")
            break

def start_chat(clientsocket, login):
    with open("messages.txt") as file:
        last_messages =  ''.join(deque(file, maxlen = 5))
    clientsocket.send(last_messages.encode(format))
    clientsocket.send('You are in chat'.encode(format))
    clientssocket.append(clientsocket)
    print(f"The user {login}  is connected")
    send_all(f"[{login}] joins the chat!", clientsocket)
    clientsocket_thread = threading.Thread(target=client_handler, args=(clientsocket, login,))
    clientsocket_thread.start()

def read_users():
    open('users.txt', 'a+')
    open('messages.txt', 'a+')
    with open('users.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            user = line.split()
            users[user[0]] = user[1]

host = '127.0.0.1'
port = 10000
format = 'utf-8'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen()
print("Server started")
clientssocket = []
users = {}
read_users()
while True:
    clientsocket, address = s.accept()
    print(f"Connected with {address}")
    get_handler = threading.Thread(target=log_in, args=(clientsocket,))
    get_handler.start()