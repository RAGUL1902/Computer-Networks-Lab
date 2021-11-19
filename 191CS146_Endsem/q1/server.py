import socket
import threading

ip = ''
port = 10000

users = {}
clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen()

# sending the message
def sendToPlayer(clientSocket, message):
    clientSocket.send(message.encode())

# recieving the info 
def recieveFromPlayer(clientSocket):
    return clientSocket.recv(1024).decode()

def sendToAll(senderSocket, message):
    for client in clients:
        if(client != senderSocket):
            sendToPlayer(client, message)

def clientConnection(clientSocket, addr, username):
    while True:
        try:
            sendToPlayer(clientSocket, "Press 1 to enter message, 2 to upload a file and 3 to download a file: ")
            option = recieveFromPlayer(clientSocket)

            if option == "1":
                message = username + " says " + clientSocket.recv(1024).decode()
                sendToAll(clientSocket, message)

            elif option == "2":
                pass

            else:
                pass

        except:
            sendToAll(clientSocket, username + " has exited the chatroom.")
            clients.remove(clientSocket)
            clientSocket.close()
            break

def connect():
    while True:
        clientSocket, addr = server.accept()
        sendToPlayer(clientSocket, "Enter the username: ")
        username = recieveFromPlayer(clientSocket)
        sendToPlayer(clientSocket, "Enter the password: ")
        password = recieveFromPlayer(clientSocket)

        if username in users.keys():
            if users[username] == password:
                sendToPlayer(clientSocket, "Successfully logged in!")
            
            else:
                clientSocket.close()
                break
        
        else:
            users[username] = password
            sendToPlayer(clientSocket, "Successfully Registered!")

        print(username, ' has connected with the server.')
        clients.append(clientSocket)
        thread = threading.Thread(target=clientConnection, args=(clientSocket, addr, username))
        thread.start()

print("Room has been created!")
connect()