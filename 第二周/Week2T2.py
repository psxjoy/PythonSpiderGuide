from bs4 import BeautifulSoup
import requests
import pymongo

client = pymongo.MongoClient('localhost', 27017)
spider = client['spider']
url_list = spider['url_list']
info_list = spider['info_list']

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/48.0.2564.116 Safari/537.36'
}


# spider 1
def get_item_links(url, pages):
    item_url = '{}o{}/'.format(url, str(pages))
    wb_data = requests.get(item_url, headers=header).text
    soup = BeautifulSoup(wb_data, 'lxml')
    if soup.find('ul', 'pageLink'):
        links = soup.select('li.js-item')
        for link in links:
            link =link.get('data-puid')
            link ='{}{}x.htm'.format(url,link)
            print(link)
            url_list.insert_one({'link': link})
    else:
        pass


# spider 2
def get_item_info(url):
    wb_data = requests.get(url, headers=header)
    if wb_data.status_code == 404:
        pass
    else:
        soup = BeautifulSoup(wb_data.text, 'lxml')
        title = soup.title.text.strip()
        Theme = soup.select('div.det-laybox span  a')[0].get_text()
        Price = soup.select(' i.f22.fc-orange.f-type')[0].get_text() + '元' if soup.find_all('i',
                                                                                            'f22 fc-orange f-type') else None
        Area = soup.select('div.leftBox > div > div > ul > li:nth-of-type(3) ')[1].get_text().replace('\n', '').replace(
            ' ',
            '')[
               6:]
        Check = list(soup.select('ul.det-infor > li:nth-of-type(1) > span')[0].stripped_strings)
        info_list.insert_one({'url': url, 'Title': title, 'Theme': Theme, 'Price': Price, 'Area': Area, 'Check': Check})

