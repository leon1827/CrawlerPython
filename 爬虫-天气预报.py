#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup

url = 'http://www.weather.com.cn/weather/101221001.shtml'
headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0',
    }
html = requests.get(url, headers=headers)
html.encoding = 'utf-8'
htmlText = html.text
soup = BeautifulSoup(html.text, 'html.parser')

# step 1： 一层层找到h1位置，先定位到l1
lis = soup.find_all('li', class_='sky skyid lv3')
data = []
weather = []
templerature = []
for li in lis:
    h1_dates = li.find_all('h1')
    p_weas = li.find_all('p', class_='wea')
    p_tems = li.find_all('p', class_='tem')

    [data.append(h1_date.text) for h1_date in h1_dates]
    [weather.append(p_wea.text) for p_wea in p_weas]
    [templerature.append(p_tem.text) for p_tem in p_tems]

print(data)
print(len(data[0]))
print(len(data[0].encode('utf-8')))
print(data[0][0])
# print(weather)
# print(templerature)

# step 2：找天气