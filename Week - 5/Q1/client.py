# Develop a code to illustrate a secure socket connection between client and server.

import socket
import ssl
import os
import time


sslServerIP = "127.0.0.1"
sslServerPort = 15001


context = ssl.SSLContext()
context.verify_mode = ssl.CERT_REQUIRED


context.load_verify_locations("./DemoCA.pem")
context.load_cert_chain(certfile="./DemoClt.crt", keyfile="./DemoClt.key")

clientSocket = socket.socket()
secureClientSocket = context.wrap_socket(clientSocket)
secureClientSocket.connect((sslServerIP, sslServerPort))

server_cert = secureClientSocket.getpeercert()
subject = dict(item[0] for item in server_cert['subject'])
commonName = subject['commonName']

if not server_cert:
    raise Exception("Unable to retrieve server certificate")

if commonName != 'DemoSvr':
    raise Exception("Incorrect common name in server certificate")

notAfterTimestamp = ssl.cert_time_to_seconds(server_cert['notAfter'])
notBeforeTimestamp = ssl.cert_time_to_seconds(server_cert['notBefore'])
currentTimeStamp = time.time()

if currentTimeStamp > notAfterTimestamp:
    raise Exception("Expired server certificate")

if currentTimeStamp < notBeforeTimestamp:
    raise Exception("Server certificate not yet active")

msgReceived = secureClientSocket.recv(1024)
print("Secure communication received from server:%s" % msgReceived.decode())

secureClientSocket.close()
clientSocket.close()
