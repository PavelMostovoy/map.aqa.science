import sys
from  bs4 import BeautifulSoup
import requests
import json
from datetime import date
import urllib.parse as parse
import psycopg2
import time
import config

try:
    with open('c_c.json','r') as f:
        data = f.read()
    c_c = json.loads(data)
    amount = 100
    to = "USD"
    values = {}
    i=0
    for key in c_c.keys():
    #print (key)
        try:
            url = "https://finance.google.com/finance/converter?a={0}&from={1}&to={2}".format(amount,key,to)
            data = requests.get(url)
            soup = BeautifulSoup(data.text,"html5lib")
            val = soup.find_all('span',{'class':'bld'})[0].text # current exchange
            values[key] = float(val.strip("U SD"))
            #print (val)
        except:
            pass
    print (values)
    file_name = str(date.today())+'.json'
    with open(file_name,'w+') as f:
        json.dump(values,f)
    # upoad partfrom
    DATABASE_URL = config.DATABASE_URL
    parse.uses_netloc.append("postgres")
    url = parse.urlparse(DATABASE_URL)
    db_name = 'currency'
    cur_date = str(date.today()).replace('-','')
    file_name = str(date.today())+'.json'
    with open(file_name,'r') as f:
        data = f.read()
    c_c = json.loads(data)
    conn = psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
        )
    cur = conn.cursor()
    try:
        cur.execute("INSERT  INTO  currency (date) VALUES (%s)",[cur_date])
    except Exception:
        pass
    conn.commit()
    cur.close()
    conn.close()
    for key in c_c.keys():
        conn = psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
        )
        cur = conn.cursor()
        try:
            cur.execute("UPDATE currency SET {0:s}  = {1}  WHERE date  =  {2} ".format(key,c_c[key],cur_date))
            conn.commit()
        except:
            pass
    cur.close()
    conn.close()
except:
    sys.exit(1)