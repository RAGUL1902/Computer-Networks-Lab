# Develop a code to illustrate a secure socket connection between client and server.

import ssl
import socket
import datetime
import time

ipAddress = "127.0.0.1"
port = 15001

serverSocket = socket.socket()
serverSocket.bind((ipAddress, port))

serverSocket.listen()
print("Server listening:")

while(True):
    (clientConnection, clientAddress) = serverSocket.accept()
    secureClientSocket = ssl.wrap_socket(clientConnection, server_side=True, ca_certs="./DemoCA.pem", certfile="./DemoSvr.crt",
                                         keyfile="./DemoSvr.key", cert_reqs=ssl.CERT_REQUIRED, ssl_version=ssl.PROTOCOL_TLSv1_2)

    client_cert = secureClientSocket.getpeercert()
    clt_subject = dict(item[0] for item in client_cert['subject'])
    clt_commonName = clt_subject['commonName']
    if not client_cert:
        raise Exception("Unable to get the certificate from the client")

    if clt_commonName != 'DemoClt':
        raise Exception("Incorrect common name in client certificate")
    t1 = ssl.cert_time_to_seconds(client_cert['notBefore'])
    t2 = ssl.cert_time_to_seconds(client_cert['notAfter'])
    ts = time.time()
    if ts < t1:
        raise Exception("Client certificate not yet active")
    if ts > t2:
        raise Exception("Expired client certificate")
    serverTimeNow = "%s" % datetime.datetime.now()
    secureClientSocket.send(serverTimeNow.encode())
    print("Securely sent %s to %s" % (serverTimeNow, clientAddress))
    secureClientSocket.close()
