# Client asks for current date
# Server responds with current date

import socket

PORT = 1234
IP = socket.gethostbyname(socket.gethostname())

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((IP, PORT))

while True:
    try:
        msgForServer = input()
        clientSocket.send(msgForServer.encode())
        msgFromServer = clientSocket.recv(1024).decode()
        print("Message from server:", msgFromServer)
    except:
        clientSocket.close()
        break
