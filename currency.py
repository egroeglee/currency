# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 10:16:30 2017
到('http://rate.bot.com.tw/xrt?Lang=zh-TW')抓取最新牌告匯率

@author: GLee
"""
import pandas
import sqlite3
dfs = pandas.read_html('http://rate.bot.com.tw/xrt?Lang=zh-TW')

# tyoe(dfs)
#len(dfs)
currency = dfs[0]
#type(currency)  得知這是一個DataFrame
#再用INDEX (ix)的方式把想要的欄位抓出來 0:5
currency = currency.ix[:, 0:5]
#調整欄位名稱 加上u 表示將文字轉為UNICODE方便之後做資料的轉換
currency.columns = [u'幣別', u'現金匯率-買入', u'現金匯率-賣出', u'即期匯率-買入', u'即期匯率-賣出']
#幣別資料名稱太長，改為取英文幣別代碼
# currency[u'幣別'].str.extract('\((USD)\)') 只改USD 進階版在下方
currency[u'幣別'] = currency[u'幣別'].str.extract('\((\w+)\)')
#可將資料轉存EXCEL currency.to_excel('currency.xlsx')
#為了將資料存進去資料庫所以加上日期是一個必要的條件
from datetime import datetime
currency['Date'] = datetime.now().strftime('%Y-%m-%d')
# currency.info() 查詢出來是DATE 是NON-NULL 接下來要改為日期時間的格式datetime64[ns](1)
currency['Date'] = pandas.to_datetime(currency['Date'])

#轉存到SQLITE
# with sqlite3.connect('C:\\Users\\GLee\\Desktop\\Crawler\\currency2.sqlite') as db:
with sqlite3.connect('D:\\Git clone\\currency-crawler\\currency2.sqlite') as db:
    currency.to_sql('currency', con = db, if_exists='append')
#也可以把資料從SQLITE轉PYTHON的格式dataframe
#with sqlite3.connect('currency.sqlite') as db:
#    df =pandas.read_sql_query('select * from currency', con = db)
#   df
"""
可以利用WIN的自動排程
"""
    