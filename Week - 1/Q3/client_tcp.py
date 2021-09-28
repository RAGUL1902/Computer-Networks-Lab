# Client and server can send and receive messages.
# Chat application.

import socket
import threading

serverIP = socket.gethostbyname(socket.gethostname())
PORT = 1234
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def receiveMessage():
    while True:
        try:
            messageReceived = clientSocket.recv(1024).decode()
            print("Message from server:", messageReceived)
        except:
            clientSocket.close()
            break


def sendMessage():
    while True:
        try:
            messageToSend = input()
            clientSocket.send(messageToSend.encode())
        except:
            clientSocket.close()
            break


def connectToServer():
    clientSocket.connect((serverIP, PORT))

    receiveMessageThread = threading.Thread(target=receiveMessage)
    receiveMessageThread.start()

    sendMessageThread = threading.Thread(target=sendMessage)
    sendMessageThread.start()


connectToServer()
