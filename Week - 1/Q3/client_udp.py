# Client and server can send and receive messages.
# Chat application.

import socket
import threading

serverName = socket.gethostbyname(socket.gethostname())
serverPort = 1234
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.connect((serverName, serverPort))


def receiveMessage():
    while True:
        try:
            msgFromServer, serverAddress = clientSocket.recvfrom(2048)
            print("Server:", msgFromServer.decode())
        except:
            clientSocket.close()
            break


def sendMessage():
    while True:
        try:
            msgForServer = input()
            clientSocket.sendto(msgForServer.encode(),
                                (serverName, serverPort))
        except:
            clientSocket.close()


clientSocket.sendto(b'',
                    (serverName, serverPort))

receiveMessageThread = threading.Thread(target=receiveMessage)
receiveMessageThread.start()

sendMessageThread = threading.Thread(target=sendMessage)
sendMessageThread.start()
