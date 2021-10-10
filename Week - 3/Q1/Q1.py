# Develop a program to print the Mail exchange servers of a particular domain with their preferences
import dns.resolver

domainName = input("Enter the input domain: ")
mxServers = dns.resolver.resolve(domainName, 'MX')


for server in mxServers:
    print(server.to_text())
