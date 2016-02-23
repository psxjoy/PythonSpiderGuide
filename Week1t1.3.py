from bs4 import BeautifulSoup
import requests

header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                 'AppleWebKit/537.36 (KHTML, like Gecko)'
                 ' Chrome/48.0.2564.109 Safari/537.36'
}
url = 'http://bj.xiaozhu.com/fangzi/1381797635.html'
web_data = requests.get(url,headers=header)
soup = BeautifulSoup(web_data.text,'lxml')
titles = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4 > em')
addresses = soup.select('div.pho_info > p')
moneys = soup.select('#pricePart > div.day_l')
pictures = soup.select('#curBigImage')
person_pictures = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')
person_names = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
person_sexs = soup.select('div.member_pic > div')


def Juage(class_name):
    if class_name == 'member_ico1':
        return '女'
    if class_name == 'member_ico':
        return '男'


for title,address,money,picture,person_name,person_picture,person_sex \
        in zip(titles,addresses,moneys,pictures, person_names,person_pictures,person_sexs):
    data = {
        'title':title.get_text().replace('\n',''),
        'address':address.get('title'),
        'money':money.get_text().replace('\n',''),
        'picture':picture.get('src'),
        'person_picture':person_picture.get('src'),
        'person_name':person_name.get_text().replace('\n',''),
        'person_sex':Juage(person_sex.get('class'))
    }

print(data)

