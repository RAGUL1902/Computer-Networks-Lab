"""
CS302 - Computer Networks Lab, Midsem Exam

Ragul N S - 191CS146

The following code is the program for the client side 
which will interact with the concurrent math server.

The client will send maths expressions to the server, 
then the server respons with the evulation of the expression. 
"""

# Importing the libraries
import socket
import threading

# Setting the socket values
serverName = socket.gethostbyname(socket.gethostname())
serverPort = 1234
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))


# Function to connect to server and then send and receive messages
while True:
    try:
        inputExp = input("Enter the expression: ")
        clientSocket.send(inputExp.encode())
        msgFromServer = clientSocket.recv(1024).decode()
        print('Message from server:', msgFromServer)
    except:
        clientSocket.close()
        break
