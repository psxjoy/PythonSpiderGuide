from bs4 import BeautifulSoup
import requests
import re

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Cookie': '
}
url = 'https://www.zhihu.com/collection/60771406'

wb_data = requests.get(url,headers=header).text
soup = BeautifulSoup(wb_data,'lxml')
pictures = soup.select('  div.zm-item-rich-text.js-collapse-body > textarea')
names = soup.select('div > a.author-link')
target_url = 'https://pic\d.zhimg.com/\w+_r.\w+'
for name,picture in zip(names,pictures):
    name = name.get_text()
    picture=picture.get_text()
    picture=re.findall(target_url,picture)
    data={
        'author':name,
        'url':picture
    }
    print(data)
