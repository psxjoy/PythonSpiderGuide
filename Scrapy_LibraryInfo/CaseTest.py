from bs4 import BeautifulSoup
import requests
import time
from classfication import get_class, get_class1

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'
}


def get_web(title):
    url = 'http://search.jd.com/Search?keyword={0}&enc=utf-8&suggest=2.his.0&book=y&wq=&pvid=i41f5ioi.tb4iki'.format(
        title)
    # time.sleep(2)
    wb_data = requests.get(url, headers=header)
    wb_data.encoding = 'UTF-8'
    soup = BeautifulSoup(wb_data.text, 'lxml')
    try:
        try:
            data_url = soup.select('#J_goodsList > ul > li:nth-of-type(1) > div > div.p-img > a')[0].get('href')
        except:
            data_url = soup.select('#J_goodsList > ul > li:nth-of-type(1) > div > div > div.gl-i-tab-content > div.tab-content-item.tab-cnt-i-selected > div.p-name > a')[0].get('href')
        data_url = 'http:' + data_url
        return get_class(data_url)
    except:
        return 'unKnown'


def get_web1(title):
    url = 'http://search.jd.com/Search?keyword={0}&enc=utf-8&suggest=2.his.0&book=y&wq=&pvid=i41f5ioi.tb4iki'.format(
        title)
    wb_data = requests.get(url, headers=header)
    wb_data.encoding = 'UTF-8'
    soup = BeautifulSoup(wb_data.text, 'lxml')
    # time.sleep(2)
    try:
        data_url = soup.select('#J_goodsList > ul > li:nth-of-type(1) > div > div.p-img > a')[0].get('href')
        data_url = 'http:' + data_url

        return get_class1(data_url)
    except:
        return 'Unknown'
