# Python program to convert domain-name to ip-address and viceversa

import socket

while True:
    option = int(
        input("1 to get ip-address\n2 to get domain-name\n3 to exit\n--> "))
    if option == 1:
        domainName = input("Enter domain-name: ")
        try:
            ipAddress = socket.gethostbyname(domainName)
            print(f'IP Adress: {ipAddress}')
        except:
            print(
                "The domain-name you entered is invalid.\nPlease follow this structure: <text>.<text>.<text>")
    elif option == 2:
        ipAddress = input("Enter IP-Address: ")
        try:
            infoFromDns = socket.gethostbyaddr(ipAddress)
            domainName = infoFromDns[0]
            print(f'Domain-Name: {domainName}')
        except:
            print("Entered IP is invalid")
    else:
        break
