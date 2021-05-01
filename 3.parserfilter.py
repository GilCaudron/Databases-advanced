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
import redis
from pymongo import MongoClient
warnings.simplefilter(action='ignore', category=Warning)

def run(runfile):
  with open(runfile,"r") as rnf:
    exec(rnf.read())


def main():
  run("3.scraper.py")
  redisClient = redis.StrictRedis(host='localhost', port=6379, db=0)
  # Retrieve the data
  blob = redisClient.get('dd')
  df_from_redis = pd.read_json(blob)
  df_from_redis.head()
  tabel2 = pd.read_json(blob)
  tabel2 = tabel2.sort_values('Amount (BTC)', ascending=False)
  df = tabel2.head(1)
  df.to_csv(r'hoogste.csv', index=False)

  client = MongoClient('localhost:27017')
  db = client.admin # client.database_name
  collection = db.bitcoin #db.collection_name

  def csv_to_json(filename, header=None):
    data = pd.read_csv(filename, header=header)
    return data.to_dict('records')

  collection.insert_many(csv_to_json('hoogste.csv', header=0))
  

while True:
  main()
  time.sleep(1*60)
