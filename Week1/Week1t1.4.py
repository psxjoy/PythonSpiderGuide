from bs4 import BeautifulSoup
import requests, urllib.request
import time
import random
url = 'http://weheartit.com/inspirations/taylorswift?scrolling=true&page=8'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/48.0.2564.109 Safari/537.36'
}

floder_path = 'C:/Users/psxjoy/PycharmProjects/MySpiderProject/Week1t1.4TaylorSwift/'
downloadurl = []
test = 1

def get_address(url, data=None):
    wb_data = requests.get(url, headers=header)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    imgs = soup.select('img')
    if data == None:
        for img in imgs:
            data = {
                'img': img.get('src')
            }
            img = img.get('src')
            downloadurl.append(img)
            print(data)
            # download_pic(downloadurl)

def download_pic(download_url):

    for item in download_url:
        urllib.request.urlretrieve(url,floder_path+str(random(1,50))+'.jpg')
        print('Done')


def get_url(start, end):
    for one in range(start, end):
        get_address(url + str(one))
        time.sleep(2)


get_url(1,6)

