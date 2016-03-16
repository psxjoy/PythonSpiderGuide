from bs4 import BeautifulSoup
import requests
import urllib.request
import re
import random

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Cookie': '=============自己的COOKIEQ！'
}
url = 'https://www.zhihu.com/collection/60771406'
floder_path='自己的文件！自己创建!记得最后的文件后面加个‘！’,比如"ZHIHU/"'
wb_data = requests.get(url,headers=header).text
soup = BeautifulSoup(wb_data,'lxml')
pictures = soup.select('  div.zm-item-rich-text.js-collapse-body > textarea')
names = soup.select('div > a.author-link')
target_url = 'https://pic\d.zhimg.com/\w+_r.\w+'
list_url = []
picture1 = ''
def download_pic(url,name):
        urllib.request.urlretrieve(url,floder_path+name+url[-8:])
        print('Done')

for name,picture in zip(names,pictures):
    name = name.get_text()
    picture=picture.get_text()
    picture=re.findall(target_url,picture)
    for i in picture:
        download_pic(i,name)
