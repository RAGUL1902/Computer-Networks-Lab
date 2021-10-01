# Program to give the top 50 rated movies details from IMDB website
# Do "pip install bs4"  for installing Beautifulsoup library
# Do "pip install lxml" for installing the lxml parser


from bs4 import BeautifulSoup
import requests
import re


def getData():
    url = "http://www.imdb.com/chart/top"
    response = requests.get(url)
    dataList = []
    soup = BeautifulSoup(response.text, 'lxml')
    movies = soup.select('td.titleColumn')
    ratings = soup.select('td.ratingColumn strong')
    crew = soup.select('td.titleColumn a')
    for i in range(0, 50):
        tempList = []
        tempList.append(' '.join(movies[i].get_text().split()))
        tempList.append(crew[i].attrs.get('title'))
        tempList.append(ratings[i].get_text())
        dataList.append(tempList)
    return dataList


dataList = getData()
for i in dataList:
    print(f'{i[0]} - {i[1]} - {i[2]}')
