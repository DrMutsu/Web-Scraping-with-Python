# -*- coding: utf-8 -*-
# @Author   : chenyao.lu 
# @FILE     : Exception_handling.py
# @Time     : 2019/11/18 17:20
# @Software : PyCharm
'''
异常处理：
http错误
https://blog.csdn.net/qq_40913582/article/details/82858024
'''
from urllib.request import urlopen,Request
from urllib import error
from bs4 import BeautifulSoup
my_header = {
             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                           '(KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
             }
## 1.检查该网页是否能请求成功
# try:
#     html = Request("https://www.bilibili.com",headers=my_header)
#     html = urlopen(html)
#     print(html.read().decode("utf-8"))
# except error.HTTPError as e:
#     print(e.code,'\n',e.reason,'\n',e.headers)
# except error.URLError as e:
#     print(e.reason)

## 2.检某一元素是否能获取成功

def get_title(url):
    try:
        html = Request(url,headers=my_header)
        html = urlopen(html)
    except error.HTTPError as e:
        print(e.code,'\n',e.reason,'\n',e.headers)
    except error.URLError as e:
        print(e.reason)
    try:
        bsobj = BeautifulSoup(html.read().decode("utf-8"),"lxml")
        title = bsobj.body.span
    except AttributeError as e:
        return None
    return title

title = get_title("http://www.bilibili.com")
if title == None:
    print("not found")
else:
    print(title)