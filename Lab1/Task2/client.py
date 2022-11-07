import socket
import threading

def get():
    while True:
        try:
            got = clientsocket.recv(1024).decode(format)
            if got == 'start':
                login = input('Login: ').strip()
                clientsocket.send(login.encode(format))
            got = clientsocket.recv(1024).decode(format)
            if got == 'log in':
                password = input('Password: ').strip()
                clientsocket.send(password.encode(format))
            elif got == 'registration':
                password = registration()
                clientsocket.send(password.encode(format))
                chat_thread = threading.Thread(target=chat, args=(login,))
                chat_thread.start()
            else:
                print(got)
        except: 
            print("An error occured!")
            clientsocket.close()
            break

def registration():
    print("Please register")
    while True:
        password = input('Password: ')
        password_confirmed = input('Confirm password: ')
        if password_confirmed == password:
            break
        print("Incorrect password, please try again")
    return password

def chat(login):
    while True:
        message = input()
        if message != "":
            clientsocket.send(f'{login}: "{message}"'.encode(format))

host = '127.0.0.1'
port = 10000
format = 'utf-8'

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((host, port))
get_handler = threading.Thread(target=get)
get_handler.start()