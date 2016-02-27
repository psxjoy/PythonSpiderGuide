from bs4 import BeautifulSoup
import requests
import pymongo
import time


client = pymongo.MongoClient('localhost',27017)
week2t2_1  = client['weeek2t2_1']
Test = week2t2_1['test']


#
# def get_info(url):
#     wb_data = requests.get(url, headers=header)
#     soup = BeautifulSoup(wb_data.text, 'lxml')
#     Titles = soup.select('#page_list > ul > li > div.result_btm_con.lodgeunitname > div > a > span')
#     Prices = soup.select('#page_list > ul > li > div.result_btm_con.lodgeunitname > span.result_price > i')
#     Comments = soup.select('#page_list > ul > li > div.result_btm_con.lodgeunitname > div > em > span')
#     # print(Comments)
#     for title, price, comment in zip(Titles, Prices, Comments):
#         data = {
#             'title': title.get_text(),
#             'price': int(price.get_text()),
#             'comment': comment.get_text()
#         }
#         Test.insert_one(data)
#
#     time.sleep(2)
#
#
# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
#                   'AppleWebKit/537.36 (KHTML, like Gecko)'
#                   ' Chrome/48.0.2564.109 Safari/537.36'
# }
#
# for page in range(1, 4):
#     url = 'http://bj.xiaozhu.com/search-duanzufang-p' + str(page) + '-0/'
#     get_info(url)
#
for item in Test.find({'price':{'$gt':800}}):
    print(item)