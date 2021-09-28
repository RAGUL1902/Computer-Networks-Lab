# Client and server can send and receive messages.
# Chat application.

import socket
import threading

port = 1234
serverIP = socket.gethostbyname(socket.gethostname())

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((serverIP, port))


def sendMessage():
    while True:
        try:
            inputMsg = input()
            serverSocket.sendto(inputMsg.encode(), clientAddress)
        except:
            serverSocket.close


def recieveMessage():
    while True:
        try:
            msgFromClient, clientAddress = serverSocket.recvfrom(2048)
            print(f'Client: {msgFromClient.decode()}')
        except:
            serverSocket.close


msgFromClient, clientAddress = serverSocket.recvfrom(2048)
messageSenderThread = threading.Thread(target=sendMessage, args=())
messageSenderThread.start()
messageRecieverThread = threading.Thread(target=recieveMessage, args=())
messageRecieverThread.start()
