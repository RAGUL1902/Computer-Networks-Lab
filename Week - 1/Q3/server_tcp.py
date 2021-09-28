# Client and server can send and receive messages.
# Chat application.

import socket
import threading


PORT = 1234
IP = socket.gethostbyname(socket.gethostname())

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((IP, PORT))
serverSocket.listen(5)


def sendMessages(clientSocket, address):
    while True:
        try:
            inputMessage = input()
            clientSocket.send(bytes(inputMessage, "utf-8"))
        except:
            clientSocket.close()


def recieveMessages(clientSocket, address):
    while True:
        try:
            receivedMessage = clientSocket.recv(1024).decode("utf-8")
            print(f"Message from client: {receivedMessage}")
        except:
            clientSocket.close()


while True:
    try:
        clientSocket, address = serverSocket.accept()
        messageSenderThread = threading.Thread(
            target=sendMessages, args=(clientSocket, address))
        messageSenderThread.start()
        messageReceiverThread = threading.Thread(
            target=recieveMessages, args=(clientSocket, address))
        messageReceiverThread.start()
    except:
        serverSocket.close()
