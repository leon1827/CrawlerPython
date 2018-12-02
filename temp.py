#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#爬取喜马拉雅音乐排行榜中所有的音乐

import requests
import json,time
from bs4 import BeautifulSoup

def xima(a):
    url = "https://www.ximalaya.com/shangye/6855034/"
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0',
    }
    html=requests.get(url,headers=headers)
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, 'html.parser')
    # 
    divlinks = soup.find_all('div', class_='text rC5T')
    for link in divlinks:
        #
        soup2 = BeautifulSoup(str(link), 'html.parser')
        alink = soup2.find('a')
        print(alink.get('href'))

if __name__ == '__main__':
    xima(1)
