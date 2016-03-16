from bs4 import BeautifulSoup
import requests
import re

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Cookie': 'q_c1=90e191c4110a445597cb9d5eb8f039e5|1457247541000|1457247541000; _za=599ad878-4d53-4051-8467-3a4c7d662c3f;'
              ' cap_id="MWU1Yzg1OTJmYTdmNDliYmIyMTZhNTc5MDNiYjRhYjM=|1457337126|fbb15b22cb660a4738f23016ceb0dfc44dbdd394";'
              ' z_c0="QUFDQVBMNFpBQUFYQUFBQVlRSlZUWDNBQkZmanVZbW5BR3kwV3JWSW1Fei1ERmZBZG15dGpnPT0=|1457337213|ae7483f43d53d536978f9cd04555563c91524aab";'
              ' _xsrf=8d5d2b8a6424d17791d59d3591432c92; udid="AFDADFtHlAmPTq-qQJW1EwYSuQbrY5zmPds=|1457510772";'
              ' __utmt=1; __utma=51854390.1908745718.1458040762.1458103416.1458105476.3;'
              ' __utmb=51854390.2.10.1458105476; __utmc=51854390;'
              ' __utmz=51854390.1458105476.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic;'
              ' __utmv=51854390.100-1|2=registration_date=20121005=1^3=entry_date=20121005=1'
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