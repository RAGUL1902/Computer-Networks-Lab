"""
CS302 - Computer Networks Lab, Midsem Exam

Ragul N S - 191CS146

The following code is the program for the server side for a concurrent math server.

The server will connect with a client and perform the required operations.
Seperate thread is created for different clients so they can act independently.
"""

# Importing the libraries
import socket
import threading


# Creating a socket for the server
serverPort = 1234
serverIP = socket.gethostbyname(socket.gethostname())
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((serverIP, serverPort))
serverSocket.listen()


# Fuction for interacting with a client
def clientThread(connectionSocket, addr):
    while True:
        try:
            msgFromClient = connectionSocket.recv(2048).decode()
            print("Message from " + str(addr) + ": " + msgFromClient)
            connectionSocket.send(str(eval(msgFromClient)).encode())
        except:
            connectionSocket.close()
            break

# Fucntion for creating a seperate thread for every connect client


def startProgram():
    while True:
        connectionSocket, addr = serverSocket.accept()
        print(addr, 'has connected with the server.')
        thread = threading.Thread(
            target=clientThread, args=(connectionSocket, addr))
        thread.start()


print('Server is ready...')
startProgram()
