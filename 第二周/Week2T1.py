from bs4 import BeautifulSoup
import requests
import time

url = 'http://bj.ganji.com/wu/'
wb_data = requests.get(url).text
soup = BeautifulSoup(wb_data,'lxml')
links =soup.select('#wrapper > div.content > div > div > dl > dt > a')
# print(links)

for link in links:
    link = 'http://bj.ganji.com'+link.get('href')
    print(link)

channel_list='''
    http://bj.ganji.com/jiaju/
    http://bj.ganji.com/rirongbaihuo/
    http://bj.ganji.com/shouji/
    http://bj.ganji.com/bangong/
    http://bj.ganji.com/nongyongpin/
    http://bj.ganji.com/jiadian/
    http://bj.ganji.com/ershoubijibendiannao/
    http://bj.ganji.com/ruanjiantushu/
    http://bj.ganji.com/yingyouyunfu/
    http://bj.ganji.com/diannao/
    http://bj.ganji.com/xianzhilipin/
    http://bj.ganji.com/fushixiaobaxuemao/
    http://bj.ganji.com/meironghuazhuang/
    http://bj.ganji.com/shuma/
    http://bj.ganji.com/laonianyongpin/
    http://bj.ganji.com/xuniwupin/
    http://bj.ganji.com/qitawupin/
    http://bj.ganji.com/ershoufree/
    http://bj.ganji.com/wupinjiaohuan/
'''