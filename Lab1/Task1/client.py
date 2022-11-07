import socket
import threading

def get():
    while True:
        try:
            message = input("Enter your message: ")
            clientsocket.send(message.encode(format))
            message = clientsocket.recv(1024).decode(format)
            print(message)
        except: 
            print("You disconnect")
            clientsocket.close()
            break

host = "127.0.0.1"
port = 10000
format = 'utf-8'

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((host, port))
get_thread = threading.Thread(target=get)
get_thread.start()
print("If you want to quit - Enter : 'Exit' ")
