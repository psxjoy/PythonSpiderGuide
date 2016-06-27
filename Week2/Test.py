from bs4 import BeautifulSoup
import requests

url = 'http://jwc.xzmc.edu.cn/wejlist.jsp?urltype=tree.TreeTempUrl&wbtreeid=1887'

wb_data = requests.get(url).text
soup=BeautifulSoup(wb_data,'lxml')
htmls = soup.select('td > a')

for i in htmls:
    print(i.get('href'))