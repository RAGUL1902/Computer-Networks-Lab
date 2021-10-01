# A http server implemented using tcp protocol
# This server responds with a basic html webpage when a request is made to it

import socket

host = "127.0.0.1"
port = 8080
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((host, port))
serverSocket.listen(5)


def createWebpage():
    webPage = "HTTP/1.1 200 OK\n\n<!DOCTYPE html>"
    webPage += "<!DOCTYPE html>"
    webPage += "\n<html>"
    webPage += "\n<head>"
    webPage += "\t<title>Response from HTTP Server</title>"
    webPage += "</head>"
    webPage += "<body>"
    webPage += "\t<h1>Hi, Welcome to this page</h1>"
    webPage += "\t<p>This is a Response webpage sent from the http server running on this local host machine at port 8080</p>"
    webPage += "</body>"
    webPage += "</html>"
    return webPage.encode()


response = createWebpage()

while True:
    try:
        clientSocket, addr = serverSocket.accept()
        requestRecieved = clientSocket.recv(1024).decode()
        print(requestRecieved)
        clientSocket.send(response)
        clientSocket.close()
    except Exception as error:
        print(error)
