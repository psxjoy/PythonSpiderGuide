#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import json
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import time

url = 'XXXXX'
header = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; MI 4LTE Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/50.0.2661.86 Mobile Safari/537.36-SuperFriday_7.4.1',
    'Cookie': 'ACNZZDATA1252894711=89097748-1465629103-%7C1465629103',
    'Content-Type': 'application/x-www-form-urlencoded'
}
data = {
    'schoolIdentity': 'XXXXX',
    's_Id': '0',
    'b_y': '2016',
    't_m': '2',
    's_n': 'XXXX',
    'p_d': 'XXXX',
    'c_k': '',
    'v_c': '',
    'identity': 'XXXX'
}

def _format_addr(s):  # 处理编码问题
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send_message(meg):  # 邮件模块
    from_addr = 'XXXXX@163.com'
    password = 'XXXXX'
    to_addr = 'XXXXX@qq.com'
    smtp_server = 'smtp.163.com'

    msg = MIMEText(meg, 'plain', 'utf-8')
    msg['From'] = _format_addr('监测系统<%s>' % from_addr)
    msg['To'] = _format_addr(' <%s>' % to_addr)
    msg['Subject'] = Header('期末成绩通知', 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()




check = ['学习']
while True:
    wb_data = requests.post(url, headers=header, data=data)
    GetList = json.loads(wb_data.text, encoding='UTF-8')
    print GetList['errorCode']
    if GetList['errorCode'] == 0:
        LengthList = len(GetList['scoreList'])
        for i in range(0, LengthList):
            CheckList = GetList['scoreList'][i]['courseName']
            CheckList = CheckList.encode('utf-8')
            if CheckList not in check:
                project = GetList['scoreList'][i]['courseName']
                project = project.encode('utf-8')
                Type = GetList['scoreList'][i]['courseProperty']
                Type = Type.encode('utf-8')
                score = GetList['scoreList'][i]['score']
                score = score.encode('utf-8')
                text = project + '成绩已经公布，成绩为：' + score +'.'
                print text
                send_message(text)
                check.append(CheckList)
    else:
        time.sleep(1800)
    time.sleep(600)
