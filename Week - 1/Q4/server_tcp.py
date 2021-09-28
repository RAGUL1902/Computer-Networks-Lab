# Clients can send messages to a server, which broadcasts it to other clients.
# Clients can receive messages from the server.
# Chat room application.

import socket
import threading

port = 1234
serverIP = socket.gethostbyname(socket.gethostname())
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((serverIP, port))
serverSocket.listen()
clientSockets = []


def sendMsgToAll(msg, senderSocket):
    for client in clientSockets:
        if client is not senderSocket:
            client.send(msg)


def waitForMsg(addr, clientSocket):
    while True:
        try:
            msgToSend = str(addr) + ': ' + clientSocket.recv(1024).decode()
            sendMsgToAll(msgToSend.encode(), clientSocket)
        except:
            msgToSend = '"'+addr+'": ' + 'left the chat'
            clientSockets.remove(clientSocket)
            clientSocket.close()
            break


def waitForClients():
    while True:
        clientSocket, address = serverSocket.accept()
        addr = str(address)
        print(f'Client "{addr}" have been connected to the room')
        clientSockets.append(clientSocket)
        msg = 'Client "' + addr + '" has entered the chat'
        sendMsgToAll(msg.encode(), clientSocket)
        recieveMsgThread = threading.Thread(
            target=waitForMsg, args=(addr, clientSocket))
        recieveMsgThread.start()


print("Server is up and running...")
waitForClients()
