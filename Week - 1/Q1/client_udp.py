# This UDP client connects to a TCP server.
# Server responds with a greeting.

import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 1234

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

clientSocket.sendto(bytes("", "utf-8"), (IP, PORT))
message, serverAddress = clientSocket.recvfrom(2048)
clientSocket.close()

print(message.decode("utf-8"))
clientSocket.close()
