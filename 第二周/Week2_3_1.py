from bs4 import BeautifulSoup
import requests
import time
import pymongo

client = pymongo.MongoClient('localhost', 27017)
ceshi = client['ceshi']
url_list = ceshi['url_list']
item_info = ceshi['item_info']


# spider_1

def get_links_from(channel, pages, who_sellers=0):
    list_view = '{}{}/pn{}/'.format(channel, str(who_sellers), str(pages))
    wb_data = requests.get(list_view)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    time.sleep(1)
    if soup.find('td', 't'):
        for link in soup.select('td.t a.t'):
            item_link = link.get('href').split('?')[0]
            url_list.insert_one({'url': item_link})
            get_item_info(list_view)
            print(item_link)
    else:
        pass
        # nothing


def get_item_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    no_longer_exist = '404' in soup.find('script', type='text/javascript').get('src').split('/')
    no_longer_exist = soup.find_all('div','error')
    if no_longer_exist:
        pass
    else:
        title = soup.title.text
        price = soup.select('span.price.c_f50')[0].text.replace('\t', '').replace('\n', '').replace(' ', '')
        date = soup.select('.time')[0].get_text()
        area = list(soup.select(' .c_25d a')[0].stripped_strings) if soup.find_all('span', 'c_25d') else None
        # item_info.insert_one({'title':title,'price':price,'date':date,'area':area})
        print({'title': title, 'price': price, 'date': date, 'area': area})


url = ' http://bj.58.com/fzixingche/'
get_links_from(url,2)