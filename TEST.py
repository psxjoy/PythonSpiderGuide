from bs4 import BeautifulSoup
import requests
import re

url = 'http://bj.58.com/pingbandiannao/24892815679312x.shtml?psid=164631328190880057818855091&entinfo=24892815679312_0'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/48.0.2564.109 Safari/537.36'
}
wb_data = requests.get(url, headers=header).text
soup = BeautifulSoup(wb_data, 'lxml').text
views_sid = re.findall('Counter58.sid="\d{2,}"', soup)  # 正则匹配查找网页中浏览量JS中的sid变量
views_info = re.findall('Counter58.infoid=\d{2,}', soup)  # 同上，朝朝infoid变量
sid = str(views_sid)[17:-3]  # 将查找到的sid变量中的无关数据剔除
infoid = str(views_info)[19:-2]  # 同上
s = 'http://jst1.58.com/counter?infoid=24925720978740&userid=&uname=&sid=509706005&lid=1&px=&cfpath=5,38484'
url_view = 'http://jst1.58.com/counter?infoid=' + infoid + '&userid=&uname=&sid=' + sid + '&lid=1&px=&cfpath=5,38484'# 拼接浏览量的js网页
url_view1 = requests.get(url_view, headers=header).text # get js网页
print(url_view1[71:])
