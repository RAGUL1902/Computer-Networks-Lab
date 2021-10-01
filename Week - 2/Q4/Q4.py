# Program to display the details of an input URL
# (status code, headers,history, encoding, reason, cookies, elapsed, request)

import requests


def startProgram():
    url = input("Enter a vaild URL: ")
    try:
        response = requests.get(url)
        printOutput(response)
    except:
        print("Entered URL is not Valid")


def printOutput(response):
    print("\n<-- Details of the Input URL -->")
    print(f'\nStatus code: {response.status_code}')
    print(f'\nHistory: {response.history}')
    print(f'\nEncoding: {response.encoding}')
    print(f'\nReason: {response.reason}')
    print(f'\nElapsed: {response.encoding}')
    print(f'\nRequest: {response.request}')

    print(f'\nCookies: ')
    for i in response.cookies:
        print(i)

    print(f'\nHeaders:')
    for key, value in response.headers.items():
        print(f'{key}: {value}')


startProgram()
