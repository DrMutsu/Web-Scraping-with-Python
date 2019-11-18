# -*- coding: utf-8 -*-
# @Author   : chenyao.lu 
# @FILE     : bs_intro.py
# @Time     : 2019/11/18 17:12
# @Software : PyCharm

'''
beautifulsoup 用于解析网页
'''
from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
my_header = {
             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                           '(KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
             }
html = Request("http://www.bilibili.com",headers=my_header)
html = urlopen(html)
bsobj = BeautifulSoup(html.read().decode("utf-8"),"lxml")
# read()方法返回的是byte类型
print(bsobj.title)