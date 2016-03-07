import requests
import json
import time
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send_message(Price):
    form_addr = '******'
    password = '*******'
    to_addr = '******'
    smtp_server = '*******'

    msg = MIMEText('摩洛哥坚果护发精油已经上架！价格:' + str(Price) + '元', 'plain', 'utf-8')
    msg['From'] = _format_addr('自动提醒<%s>' % form_addr)
    msg['To'] = _format_addr(' <%s>' % to_addr)
    msg['Subject'] = Header('摩洛哥精油上架提醒', 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(form_addr, password)
    server.sendmail(form_addr, [to_addr], msg.as_string())
    server.quit()


header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/48.0.2564.109 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': ###省略部分隐私数据
}
data = {  # 摩洛哥精油数据
    '_mt': 'b2cmall.getProductHotData',
    'itemId': '10780',
    '_sm': 'md5',
    '_aid': '1',
    '_sig': '5fc1d3ab173bb79b8dd05df36867bc70'
}
data1 = {  # 摩洛哥Ligth精油数据
    '_mt': 'b2cmall.getProductHotData',
    'itemId': '10781',
    '_sm': 'md5',
    '_aid': '1',
    '_sig': '1e0aea8dff1165199a0ad8d1c8cdeb43'
}


def get_info(data):  # 判断 True为缺货
    url = requests.post('http://www.fengqu.com/m.api', data=data, headers=header)
    text = url.text
    text = json.loads(text)
    text = text['content']
    Juage = text[0]['soldOut']
    Price = text[0]['sellingPrice'] / 100
    return Juage


def get_Price(data):  # 得到商品价格
    url = requests.post('http://www.fengqu.com/m.api', data=data, headers=header)
    text = url.text
    text = json.loads(text)
    text = text['content']
    Price = text[0]['sellingPrice'] / 100
    return Price


def should_send_email(email_sent, item_):  # 判断是否发送邮件
    return (not item_) and (not email_sent)


email_sent = False

while True:
    if should_send_email(email_sent, get_info(data)):
        send_message(get_Price(data))
        email_sent = True
    time.sleep(30)
    if should_send_email(email_sent, get_info(data1)):
        send_message(get_Price(data1))
        email_sent = True

