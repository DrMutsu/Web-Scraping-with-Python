# -*- coding: utf-8 -*-
# @Author   : chenyao.lu 
# @FILE     : ComplexHTMLparsing.py
# @Time     : 2019/11/20 11:23
# @Software : PyCharm
"""
复杂网页的解析
"""
from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
my_header = {
             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                           '(KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
             }
html = Request("http://www.pythonscraping.com/pages/warandpeace.html",headers=my_header)
html = urlopen(html)
bsobj = BeautifulSoup(html,"lxml")
namelist = bsobj.findAll("span", {"class":"green"}) # <span> 元素对文本中的一部分进行着色
# for name in namelist:
#     print(name.get_text())

# 同时查找多个标签
# print(bsobj.findAll({"h1","h2"}))

# 查找一个标签下的多个属性内容
# print(bsobj.findAll("span", {"class":{"green","red"}}))

# 按照文本内容查找
# prince = bsobj.findAll(text="the prince")
# print(len(prince))

# id
# alltext = bsobj.findAll(id="text")
# print(alltext[0].get_text())

