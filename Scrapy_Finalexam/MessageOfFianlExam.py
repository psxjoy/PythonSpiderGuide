#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import requests
import urllib
import time
import sys
import httplib

reload(sys)
sys.setdefaultencoding("utf-8")

url = 'XXXXXX'
header = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; MI 4LTE Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/50.0.2661.86 Mobile Safari/537.36-SuperFriday_7.4.1',
    'Cookie': 'ACNZZDATA1252894711=89097748-1465629103-%7C1465629103',
    'Content-Type': 'application/x-www-form-urlencoded'
}
data = {
    'schoolIdentity': 'XXXX',
    's_Id': '0',
    'b_y': '2016',
    't_m': '2',
    's_n': 'XXX',
    'p_d': 'XXX',
    'c_k': '',
    'v_c': '',
    'identity': 'XXXX'
}


def send_sms(apikey, text, mobile):
    sms_host = "sms.yunpian.com"
    port = 443
    version = "v2"
    sms_send_uri = "/" + version + "/sms/single_send.json"
    params = urllib.urlencode({'apikey': apikey, 'text': text, 'mobile': mobile})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = httplib.HTTPSConnection(sms_host, port=port, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str

apikey = 'XXXXX'
mobile = XXXXX

check = ['学习']
while True:
    wb_data = requests.post(url, headers=header, data=data)
    GetList = json.loads(wb_data.text, encoding='UTF-8')
    print GetList['errorCode']
    if GetList['errorCode'] == 0:
        LengthList = len(GetList['scoreList'])
        for i in range(0, LengthList):
            CheckList = GetList['scoreList'][i]['courseName']
            if CheckList not in check:
                project = str(GetList['scoreList'][i]['courseName'])
                type = str(GetList['scoreList'][i]['courseProperty'])
                score = str(GetList['scoreList'][i]['score'])
                text = '【淮工期末成绩通】可爱的XXX,您的' + project + '成绩已经公布，成绩为：' + score + '。课程属性：' + type + '.'
                print text
                print send_sms(apikey=apikey, text=text, mobile=mobile)
                check.append(CheckList)
    else:
        time.sleep(60)
    time.sleep(60)
