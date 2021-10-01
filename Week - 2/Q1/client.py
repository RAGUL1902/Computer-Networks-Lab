# A client program which sends a http request to the http server via a tcp connection
# The response then recieved is printed in the terminal

import socket

host = "127.0.0.1"
port = 8080
request = f"GET / HTTP/1.1\r\nHost: {host}:{port}\r\n\r\n".encode()
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((host, port))
clientSocket.send(request)
response = clientSocket.recv(1024)
print(response)
