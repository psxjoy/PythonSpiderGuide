from bs4 import BeautifulSoup
import requests
import pymongo
import time

client = pymongo.MongoClient('localhost',27017)
spider = client['spider']
url_list = spider['url_list']
info_list = spider['info_list']

#spider 1
def get_item_links(url,pages):
    item_url = '{}o{}/'.format(url,str(pages))
    wb_data = requests.get(item_url).text
    soup = BeautifulSoup(wb_data,'lxml')
    links = soup.select('#wrapper > div.leftBox > div.layoutlist > dl > dd.feature > div > ul > li')
    for link in links:
        link = '{}{}x.htm'.format(url,link.get('data-puid'))

#spider 2
def get_item_info(url):
    wb_data = requests.get(url).text
    soup = BeautifulSoup(wb_data,'lxml')
    title = soup.select('.title-name')[0].get_text()
    Theme = soup.select('#wrapper > div.content.clearfix > div.leftBox > div > div > ul > li > span > a')[0].get_text()
    Price = soup.select('#wrapper > div.content.clearfix > div.leftBox > div > div > ul > li > i.f22.fc-orange.f-type')[0].get_text()


