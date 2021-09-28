# Clients can send messages to a server, which broadcasts it to other clients.
# Clients can receive messages from the server.
# Chat room application.

import socket
import threading

serverPort = 1234
serverIP = socket.gethostbyname(socket.gethostname())
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((serverIP, serverPort))
clients = []


def sendToAll(message, senderClientAddress):
    for clientAddress in clients:
        if str(clientAddress) != str(senderClientAddress):
            serverSocket.sendto(message.encode(), clientAddress)


def receiveMsgFromClient():
    while True:
        msgFromClient, currClient = serverSocket.recvfrom(2048)

        if currClient not in clients:
            clients.append(currClient)
            msgToSend = (str(currClient) + ' entered the chatroom.')
        else:
            msgToSend = str(currClient) + ': ' + msgFromClient.decode()

        sendToAll(msgToSend, str(currClient))


print('Server is ready to welcome clients.')
receiveMsgFromClient()
