from bs4 import BeautifulSoup
import requests
import psycopg2
from datetime import date
from urllib import parse
import config

# url = "https://finance.yahoo.com/quote/CL=F/"
url = "https://wog.ua/ua/map/"

data = requests.get(url)
soup = BeautifulSoup(data.text, "html")


# soup.find_all("var pointsJSON =(.+?)]';")

rawJ = soup.find_all('script')
J = str(rawJ[23])
J1 = J.split('var pointsJSON = ')
# J2 = J1[1].rsplit('var record =')
J1 = J1[0].rsplit('},{', 1)

# JsonText = J3[0].decode('utf-8')



#
#
#
# t = soup.find_all('div',{'class':'My(6px) smartphone_Mt(15px)'})
#
# cur_date = str(date.today()).replace('-','')
#
# val = t[0].find_all('span',{'data-reactid':'14'})[0].text
#
# DATABASE_URL = config.DATABASE_URL
#
# parse.uses_netloc.append("postgres")
# url = parse.urlparse(DATABASE_URL)
#
#
#
# conn = psycopg2.connect(
#         database=url.path[1:],
#         user=url.username,
#         password=url.password,
#         host=url.hostname,
#         port=url.port
#     )
# cur = conn.cursor()
# try:
#     cur.execute("UPDATE currency SET brent_crude  = {}  WHERE date  =  {} ".format(val,cur_date))
#     conn.commit()
# except:
#     pass
# cur.close()
# conn.close()