from bs4 import BeautifulSoup

info = []
with open('D:/Python/week1/new_index.html','r')as wb_date:
    Soup = BeautifulSoup(wb_date,'lxml')
    images = Soup.select(
        'body > div.main-content > ul > li > img')
    titles = Soup.select(
        'body > div.main-content > ul > li > div.article-info > h3 > a')
    descs = Soup.select(
        'body > div.main-content > ul > li > div.article-info > p.description')
    rates = Soup.select(
        'body > div.main-content > ul > li > div.rate > span')
    cates = Soup.select(
        'body > div.main-content > ul > li > div.article-info > p.meta-info')
    # print(images,titles,descs,rates,cates,sep='\n----------------\n')

for image,title,desc,rate,cate in zip(images,titles,descs,rates,cates):
    date = {
        'title':title.get_text(),
        'desc':desc.get_text(),
        'rate':rate.get_text(),
        'cate':list(cate.stripped_strings),
        'image':image.get('src')
    }
    info.append(date)


for i in info:
    if float(i['rate'])>3:
        print(i['title'],i['cate'])
