# A UDP client connects to a UDP server.
# Server responds with a greeting.

import socket

PORT = 1234
IP = socket.gethostbyname(socket.gethostname())

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((IP, PORT))


while True:
    print(f"Waiting for new client..")
    msgFromClient, clientAddress = serverSocket.recvfrom(1024)
    print(
        f"Connected to Client of address {clientAddress[0]}.\nGreetings message sent to client.\n")

    serverSocket.sendto(
        bytes("Greeting! This message is from server\n", "utf-8"), clientAddress)
