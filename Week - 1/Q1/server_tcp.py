# A TCP client connects to a TCP server.
# Server responds with a greeting.

import socket

PORT = 1234
IP = socket.gethostbyname(socket.gethostname())

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((IP, PORT))

serverSocket.listen(5)

while True:
    print(f"Waiting for new client..")
    clientSocket, clientAddress = serverSocket.accept()
    print(
        f"Connected to Client of address {clientAddress[0]}.\nGreetings message sent to client.\n")
    clientSocket.send(
        bytes("Greetings ! This message is from server.\n", "utf-8"))
