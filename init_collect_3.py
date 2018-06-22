from bs4 import BeautifulSoup
import requests
import psycopg2
from datetime import date
from urllib import parse
import config

url = "https://wog.ua/ua/map/"

data = requests.get(url)
soup = BeautifulSoup(data.text, "html")


rawJ = soup.find_all('script')
J = str(rawJ[23])
J1 = J.split('var pointsJSON = ')
J2 = J1[1]

print(J2)