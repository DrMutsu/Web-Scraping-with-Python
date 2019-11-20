# -*- coding: utf-8 -*-
# @Author   : chenyao.lu 
# @FILE     : NaviTree.py
# @Time     : 2019/11/20 11:56
# @Software : PyCharm

'''
beautifulsoup总是处理当前标签的后代标签
后代标签范围比子标签广
实验网页是一个购物网站，有许多层级
http://www.pythonscraping.com/pages/page3.html
https://www.jianshu.com/p/043db7dd7ecf
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

# .children 找出所有子标签  descendants()找出后代标签
# 换行符也当成节点，需要去掉
# for child in bsobj.find("table", {"id":"giftList"}).children:
#     if child != "\n":
#         print(child)
#         print("-"*20)
# for descendant in bsobj.find("table", {"id":"giftList"}).descendants:
#     print(descendant)

# 兄弟标签
# for sibling in bsobj.find("table", {"id":"giftList"}).tr.next_siblings:
#     print(sibling)
# for sibling in bsobj.find("tr", {"id":"gift2"}).previous_siblings:
#     print(sibling)
#     print("-"*20)
# print(bsobj.find("tr", {"id":"gift2"}).previous_sibling)

# 父标签
'''
Python爬虫获取html中的文本方法多种多样，这里主要介绍一下string、strings、stripped_strings和get_text用法

string：用来获取目标路径下第一个非标签字符串，得到的是个字符串

strings：用来获取目标路径下所有的子孙非标签字符串，返回的是个生成器

stripped_strings：用来获取目标路径下所有的子孙非标签字符串，会自动去掉空白字符串，返回的是一个生成器

get_text：用来获取目标路径下的子孙字符串，返回的是字符串（包含HTML的格式内容）

text：用来获取目标路径下的子孙非标签字符串，返回的是字符串

原文链接：https://blog.csdn.net/qq_22592457/article/details/100597190
'''
# print(bsobj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.text.replace("\n", "").strip())

