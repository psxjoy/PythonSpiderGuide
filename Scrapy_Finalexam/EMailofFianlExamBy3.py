import json
import requests
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import time

url = 'XXXXXX'
header = {  # header模拟浏览器浏览
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; MI 4LTE Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/50.0.2661.86 Mobile Safari/537.36-SuperFriday_7.4.1',
    'Cookie': 'ACNZZDATA1252894711=89097748-1465629103-%7C1465629103',
    'Content-Type': 'application/x-www-form-urlencoded'
}
data = {  # 传递验证信息
    'schoolIdentity': 'XXXXX',
    's_Id': '0',
    'b_y': '2015',
    't_m': '2',
    's_n': 'xxx',  # 这里输入你的学号
    'p_d': 'xxx',  # 这里输入你的密码
    'c_k': '',
    'v_c': '',
    'identity': 'XXXXXS'
}


def _format_addr(s):  # 处理编码问题
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send_message(meg):  # 邮件模块
    form_addr = 'xxx@xxxx.com'
    password = 'xxx'
    to_addr = 'xxxxx@139.com'
    smtp_server = 'xxx.xxx.com'

    msg = MIMEText(meg, 'plain', 'utf-8')
    msg['From'] = _format_addr('成绩提醒<%s>' % form_addr)
    msg['To'] = _format_addr(' <%s>' % to_addr)
    msg['Subject'] = Header('期末成绩', 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(form_addr, password)
    server.sendmail(form_addr, [to_addr], msg.as_string())
    server.quit()


check = ['test']  # 随便创建某一个数组
while True:
    wb_data = requests.post(url,headers=header,data=data)
    GetList = json.loads(wb_data.text)
    if GetList['errorCode']==0:
        LengthList = len(GetList['scoreList'])
        for i in range(0,LengthList):
            CheckList = GetList['scoreList'][i]['courseName']
            if CheckList not  in check:
                Subject = str(GetList['scoreList'][i]['courseName'])
                Theme = str(GetList['scoreList'][i]['courseProperty'])
                Score = str(GetList['scoreList'][i]['score'])
                meg = '您的' + Subject + '(' + Theme + ')成绩已经公布，成绩为' + Score                
                send_message(meg)
                check.append(CheckList)
    else:
        time.sleep(3600)
    time.sleep(600)
