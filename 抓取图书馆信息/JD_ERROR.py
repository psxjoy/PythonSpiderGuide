from bs4 import BeautifulSoup
import re
import requests
from test import get_web, get_web1
import pymongo
import time

client = pymongo.MongoClient('localhost', 27017)
Library = client['Library']
info = Library['info']

for i in info.find():
    print(i['Tag'][0])