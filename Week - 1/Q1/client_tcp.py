# This TCP client connects to a TCP server.
# Server responds with a greeting.

import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 1234

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((IP, PORT))

message = clientSocket.recv(1024)
print(message.decode("utf-8"))
