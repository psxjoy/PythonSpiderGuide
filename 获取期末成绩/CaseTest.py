import json
import requests
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import time

url = 'http://112.124.54.19/Score/score/importScoreFromSchool.action'
header = {
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0.1; MI 4LTE Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/50.0.2661.86 Mobile Safari/537.36-SuperFriday_7.4.1',
    'Cookie':'ACNZZDATA1252894711=89097748-1465629103-%7C1465629103',
    'Content-Type':'application/x-www-form-urlencoded'
}
data = {
    'schoolIdentity':'7D6F7B500C3C8AE89C0ED9362898CD0F',
    's_Id':'0',
    'b_y':'2015',
    't_m':'2',
    's_n':'XXX',
    'p_d':'XXX',
    'c_k':'',
    'v_c':'',
    'identity':'E0C90E6559BB6E23212F197976DE9A1B'
}
wb_data = requests.post(url,headers=header,data=data)
print(wb_data.text)