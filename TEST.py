from bs4 import BeautifulSoup
import requests
import re
url = 'http://bj.58.com/pingbandiannao/25125976792746x.shtml?psid=164631328190880057818855091&entinfo=25125976792746_0'

header={
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/48.0.2564.109 Safari/537.36'
}
def get_info(url):
    wb_data = requests.get(url,headers=header)
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles = soup.select('div.per_ad_left > div.col_sub.mainTitle > h1')
    Themes = soup.select(' div.breadCrumb.f12 > span:nth-of-type(3) > a')
    Prices = soup.select(' div.per_ad_left > div.col_sub.sumary > ul > li:nth-of-type(1) > div.su_con > span')
    Goods = soup.select(' div.per_ad_left > div.col_sub.sumary > ul > li:nth-of-type(2) > div.su_con > span')
    Areas = soup.select('div.per_ad_left > div.col_sub.sumary > ul > li:nth-of-type(3) > div.su_con > span  ')
    dates = soup.select('#index_show > ul.mtit_con_left.fl > li.time')
    for title,theme,price,good,area,date in zip(titles,Themes,Prices,Goods,Areas,dates):
        data = {
            '标题':title.get_text(),
            '类目':theme.get_text(),
            '价格':price.get_text(),
            '成色':good.get_text().replace('\t','').replace('\n','').replace(' ',''),
            '区域':area.get_text().replace('\t','').replace('\n',''),
            '发帖日期':date.get_text(),
        }
        print(data)