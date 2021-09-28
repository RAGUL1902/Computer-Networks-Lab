# Client asks for current date
# Server responds with current date

import socket
import datetime

PORT = 1234
IP = socket.gethostbyname(socket.gethostname())

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((IP, PORT))

serverSocket.listen(5)

clientSocket, address = serverSocket.accept()

while True:
    try:
        messageRecieved = clientSocket.recv(1024).decode()
        print("Message from client:", messageRecieved)
        if messageRecieved.lower().find('date') == -1:
            messageToBeSent = 'Enter \'date\' to receive today\'s date!'
            clientSocket.send(messageToBeSent.encode())
        else:
            messageToBeSent = str(datetime.date.today())
            clientSocket.send(messageToBeSent.encode())
    except:
        clientSocket.close()
        break
