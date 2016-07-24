from bs4 import BeautifulSoup
import requests
import re
import urllib
import time
import random
url = 'https://www.zhihu.com/collection/61633672?page='  # 收藏夹地址
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Cookie': ''
    }
floder_path = "D:/TEST/知乎妹子/"  # 图片保存地址
endnum = 41  # 收藏夹页数+1


def download_pic(url, name):
    urllib.request.urlretrieve(url, floder_path + name +url[-8:] )


for i in range(1, endnum):
    time.sleep(2)
    url_page = url + str(i)
    wb_data = requests.get(url_page, headers=header).text
    soup = BeautifulSoup(wb_data, 'lxml')
    pictures = soup.select('  div.zm-item-rich-text.js-collapse-body > textarea')
    names = soup.select('div > a.author-link')
    target_url = 'https://pic\d.zhimg.com/\w+_r.\w+'
    list_url = []
    picture1 = ''

    for name, picture in zip(names, pictures):
        name = name.get_text()
        picture = picture.get_text()
        picture = re.findall(target_url, picture)
        for i in picture:
            download_pic(i, name)

print('抓取结束!')
