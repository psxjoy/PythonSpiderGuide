from bs4 import BeautifulSoup
import requests


headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36',
    'Cookie':'ASP.NET_SessionId=1zh5syzxxhogywuzatun2455'
}

url = 'http://jwby.hyit.edu.cn/xs_main.aspx?xh=1141314818'
wb_date = requests.get(url,headers=headers)
Soup = BeautifulSoup(wb_date.text,'lxml')
titles = Soup.select('#headDiv')
print(Soup)