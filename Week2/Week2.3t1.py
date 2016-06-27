from bs4 import BeautifulSoup
import requests
import pymongo


client = pymongo.MongoClient('localhost',27017)
Tnum = client['Tnum']
TTnum = Tnum['TTnum']

url = 'http://bj.58.com/shoujihao/?PGTID=0d200005-0000-1224-1b55-5cd573f905ed&ClickID=1'

wb_data= requests.get(url).text
soup = BeautifulSoup(wb_data,'lxml')
nums = soup.select('.number')
titles = soup.select('.red_adinfo')

for num,title in zip( nums,titles):
    data ={
        'Number':num.get_text(),
        'Title':title.get_text()
    }
    TTnum.insert_one(data)
for item in TTnum.find():
    print(item)