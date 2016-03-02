from bs4 import BeautifulSoup
import requests

url = 'http://bj.ganji.com/jiaju/1916072137x.htm'

wb_data = requests.get(url).text
soup = BeautifulSoup(wb_data,'lxml')
title = soup.select('.title-name')[0].get_text()
Theme = soup.select('div.det-laybox span  a')[0].get_text()
Price = soup.select(' i.f22.fc-orange.f-type')[0].get_text()
Area = soup.select('div.leftBox > div > div > ul > li:nth-of-type(3) ')[1].get_text().replace('\n','')
print(Area)
