# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 11:05:20 2017
將牌告匯率寄送EMAIL
@author: GLee
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

pw = 'George0822'
fromaddr = 'egroeggee@gmail.com'
toaddr = 'egroeglee@gmail.com'
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['subject'] = '[牌告匯率通知]'
#讀取SQLITE資料
import sqlite3, pandas
with sqlite3.connect('C:\\Users\\GLee\\Desktop\\Crawler\\currency2.sqlite') as db:
    df =pandas.read_sql_query(r'select * from currency where "幣別" = "JPY" order by Date limit 1', con = db)

#body = '牌告匯率通知'
#msg.attach(MIMEText(body, 'plain'))
msg.attach(MIMEText(df.to_html(), 'html'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, pw)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()


