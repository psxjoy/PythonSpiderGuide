from bs4 import BeautifulSoup
import re
import requests
from test import get_web, get_web1
import pymongo
import time

client = pymongo.MongoClient('localhost', 27017)
Library = client['Library']
info = Library['info']

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'
}


def get_info(url):
    wb_data = requests.get(url, headers=header)
    wb_data.encoding = 'UTF-8'
    soup = BeautifulSoup(wb_data.text, 'lxml')

    Titles = soup.select('#container > table  > tr > td:nth-of-type(2)')
    Authors = soup.select('#container > table  > tr > td:nth-of-type(3)')
    Publishers = soup.select('#container > table  > tr > td:nth-of-type(4)')
    Dates = soup.select('#container > table  > tr > td:nth-of-type(5)')
    Status = soup.select('#container > table  > tr > td:nth-of-type(6)')
    Notes = soup.select('#container > table  > tr > td:nth-of-type(7)')

    for title, author, publisher, date, statue, note in zip(Titles, Authors, Publishers, Dates, Status, Notes):
        title = title.get_text()
        final_title = re.sub(r"\W", "", title)
        author = author.get_text().replace(' ', '')
        publisher = publisher.get_text()
        final_publisher = re.sub(r"\d|\W", "", publisher)
        date = date.get_text().replace(' ', '')
        statue = statue.get_text().replace(' ', '')
        note = note.get_text().replace(' ', '')
        if note == '':
            note = 'None'
        data = {
            '书名': final_title,
            '作者': author,
            '出版社': final_publisher,
            '推荐日期': date,
            '荐购状态': statue,
            '备注': note
        }
        if data['书名'] == '题名':
            continue
        else:
            # print(get_web1(final_title))
            print(get_web(final_title))
            print(final_title)

            #
            # info.insert_one({
            #     '书名': final_title,
            #     '作者': author,
            #     '出版社': final_publisher,
            #     '推荐日期': date,
            #     '荐购状态': statue,
            #     '备注': note,
            #     'Tag': (get_web(final_title), get_web1(final_title))})


def get_url():
    for i in range(1, 3):
        url = 'http://opac.hyit.edu.cn/asord/asord_hist.php?page={0}'.format(i)
        # time.sleep(10)
        get_info(url)


if __name__ == '__main__':
    get_url()

print('Ok')
