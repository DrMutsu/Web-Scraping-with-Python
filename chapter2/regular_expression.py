# -*- coding: utf-8 -*-
# @Author   : chenyao.lu 
# @FILE     : regular_expression.py
# @Time     : 2019/11/20 15:36
# @Software : PyCharm
'''
正则表达式
lambda表达式
获取属性：Tag.attrs["src"]

'''
from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
my_header = {
             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                           '(KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
             }
html = Request("http://www.pythonscraping.com/pages/page3.html",headers=my_header)
html = urlopen(html)
bsobj = BeautifulSoup(html,"lxml")