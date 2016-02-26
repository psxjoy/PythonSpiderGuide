from bs4 import BeautifulSoup
import requests
import re

list_url = 'http://bj.58.com/pbdn/0/'  # 商品列表
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/48.0.2564.109 Safari/537.36'
}


def get_info(url):  # 获取最终信息
    wb_data = requests.get(url, headers=header)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    views = soup.text  # 浏览量预处理
    Titles = soup.select('div.per_ad_left > div.col_sub.mainTitle > h1')  # 商品标题
    Themes = soup.select(' div.breadCrumb.f12 > span:nth-of-type(3) > a')  # 商品类型
    Prices = soup.select(' div.per_ad_left > div.col_sub.sumary > ul > li:nth-of-type(1) > div.su_con > span')  # 商品价格
    Goods = soup.select(' div.per_ad_left > div.col_sub.sumary > ul > li:nth-of-type(2) > div.su_con > span')  # 商品成色
    Areas = soup.select('div.per_ad_left > div.col_sub.sumary > ul > li:nth-of-type(3) > div.su_con > span  ')  # 商品区域
    dates = soup.select('#index_show > ul.mtit_con_left.fl > li.time')  # 发帖时间
    for title, theme, price, good, area, date, view in zip(Titles, Themes, Prices, Goods, Areas, dates, views):
        data = {
            '标题': title.get_text(),
            '类目': theme.get_text(),
            '价格': price.get_text(),
            '成色': good.get_text().replace('\t', '').replace('\n', '').replace(' ', ''),  # 处理换行符和空格等不相关的字符
            '区域': area.get_text().replace('\t', '').replace('\n', ''),  # 同上
            '发帖日期': date.get_text(),
            '浏览人数': get_views(views),  # 执行get_views()函数，获取浏览量
        }
        print(data)


def get_views(views):  # 获取浏览人数
    views_sid = re.findall('Counter58.sid="\d{2,}"', views)  # 正则匹配查找网页中浏览量JS中的sid变量
    views_info = re.findall('Counter58.infoid=\d{2,}', views)  # 同上，朝朝infoid变量
    sid = str(views_sid)[17:-3]  # 将查找到的sid变量中的无关数据剔除
    infoid = str(views_info)[19:-2]  # 同上
    s = 'http://jst1.58.com/counter?infoid=24925720978740&userid=&uname=&sid=509706005&lid=1&px=&cfpath=5,38484'
    url_view = 'http://jst1.58.com/counter?infoid=' + infoid + '&userid=&uname=&sid=' + sid + '&lid=1&px=&cfpath=5,38484'# 拼接浏览量的js网页
    url_view1 = requests.get(url_view, headers=header).text # get js网页
    get_view = url_view1[71:]
    return get_view


wb_data = requests.get(list_url, headers=header)

soup = BeautifulSoup(wb_data.text, 'lxml')

titles = soup.select(' td.t > a')

final_web = ''  # 正确商品信息

# search_url为正则表达式获取正确的网址
search_url = 'http://bj.58.com/pingbandiannao/\d{2,}x.shtml\?psid=\d{20,}&entinfo=\d{10,}_0'
for title in titles:  # 查找要爬起的内容
    wb_title = title.get('href')
    wb_final = re.findall(search_url, wb_title)  # 正则查找符合标准的链接
    if len(wb_final) == 0:  # 处理list中剔除的空值
        continue
    else:
        final_web = final_web.join(wb_final)  # 将list转换为string类型变量，得到最终的商品网址
        get_info(final_web)  # 执行get_info函数，得到商品详细信息
