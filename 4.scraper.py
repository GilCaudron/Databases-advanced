import bs4
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import urllib
import re
import os
import time
import warnings
from pymongo import MongoClient
import redis

warnings.simplefilter(action='ignore', category=Warning)


r = requests.get('https://www.blockchain.com/btc/unconfirmed-transactions')
soup = bs4.BeautifulSoup(r.text,'html.parser')
content = soup.find('div', {"class": "sc-20ch6p-0 beTSoK"})
content2 = content.get_text()

content3 = (content2.replace('Hash','\nHash'))
content4 = (content3.replace('Time', ' Time'))
content5 = (content4.replace('Amount', ' Amount'))
content6 = (content5.replace(',', ''))
content7 = (content6.replace(' ', ','))
content8 =  (content7.replace('Amount,(BTC)', 'Amount (BTC)'))
content9 =  (content8.replace(',BTC,Amount,(USD)', ' BTC,Amount (USD)'))
content10 =  (content9.replace('Amount,(USD)', 'Amount (USD)'))

file = open('blockchain.csv', 'w+')
print(content10, file=open("blockchain.csv", "a"))

with open('blockchain.csv', 'r') as fin:
    data = fin.read().splitlines(True)
with open('blockchain.csv', 'w') as fout:
    fout.writelines(data[1:])
with open('blockchain.csv', 'r') as file :
  filedata = file.read()
filedata = filedata.replace('(USD),', '(USD)')
with open('blockchain.csv', 'w') as file:
  file.write(filedata)
tabel = pd.read_csv('blockchain.csv')
tabel['Time'] = tabel['Time'].str.replace(r'Time', '')
tabel['Amount (BTC)'] = tabel['Amount (BTC)'].str.replace(r'Amount', '')
tabel['Amount (BTC)'] = tabel['Amount (BTC)'].str.replace(r'(', '')
tabel['Amount (BTC)'] = tabel['Amount (BTC)'].str.replace(r')', '')
tabel['Amount (BTC)'] = tabel['Amount (BTC)'].str.replace(r'BTC', '')
tabel['Amount (USD)'] = tabel['Amount (USD)'].str.replace(r'Amount', '')
tabel['Amount (USD)'] = tabel['Amount (USD)'].str.replace(r'USD', '')
tabel['Amount (USD)'] = tabel['Amount (USD)'].str.replace(r'(', '')
tabel['Amount (USD)'] = tabel['Amount (USD)'].str.replace(r')', '')
tabel['Amount (BTC)'] = tabel['Amount (BTC)'].astype(float)
tabel['Amount (USD)'] = tabel['Amount (USD)'].str.replace(r' ', '')
warnings.simplefilter(action='ignore', category=Warning)
tabel.to_csv(r'blockchain.csv', index=False)

redisClient = redis.StrictRedis(host='localhost', port=9000, db=0)
# Create dataframe
dd = tabel
df = pd.DataFrame(dd)
data = df.to_json()
redisClient.set('dd', data)


