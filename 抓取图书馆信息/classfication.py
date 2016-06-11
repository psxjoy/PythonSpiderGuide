from bs4 import BeautifulSoup
import requests

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'
}


def get_class(url):

    wb_data = requests.get(url, headers=header)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    Class = soup.select('#root-nav > div > div > span:nth-of-type(1) > a:nth-of-type(1)')[0].get_text()
    return Class


def get_class1(url):

    wb_data = requests.get(url, headers=header)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    Class1 = soup.select('#root-nav > div > div > span:nth-of-type(1) > a:nth-of-type(2)')[0].get_text()
    return Class1
