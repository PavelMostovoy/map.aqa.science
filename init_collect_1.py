from bs4 import BeautifulSoup
import requests
import psycopg2
from datetime import date
from urllib import parse
import config

url = "https://finance.yahoo.com/quote/CL=F/"

data = requests.get(url)
soup = BeautifulSoup(data.text, "html5lib")
t = soup.find_all('div',{'class':'My(6px) smartphone_Mt(15px)'})

cur_date = str(date.today()).replace('-','')

val = t[0].find_all('span',{'data-reactid':'14'})[0].text

DATABASE_URL = config.DATABASE_URL

parse.uses_netloc.append("postgres")
url = parse.urlparse(DATABASE_URL)



conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )
cur = conn.cursor()
try:
    cur.execute("UPDATE currency SET brent_crude  = {}  WHERE date  =  {} ".format(val,cur_date))
    conn.commit()
except:
    pass
cur.close()
conn.close()