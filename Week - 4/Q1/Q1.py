#  A basic port scanner to check if particular ports are open or closed for an input remote host.

import socket

newSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
targetMachine = input("Input the website to scan: ")
openPorts = []


def portScan(portNumber):
    try:
        connection = newSocket.connect((targetMachine, portNumber))
        return True
    except:
        return False


print("Scaning 100 ports -", end="")
for portNumber in range(1, 101):
    print("#", end="")
    if portScan(portNumber):
        openPorts.append(portNumber)

print("\nThe open ports are: ", end="")
for i in openPorts:
    print(f'{i} ', end="")
