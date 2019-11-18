from urllib.request import urlopen,Request
# 没有加入头部，有的网址需要加入头部才可以访问成功
my_header = {
             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                           '(KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
             }
html = Request("http://www.bilibili.com",headers=my_header)
html = urlopen(html)
# read()方法返回的是byte类型
print(html.read().decode("utf-8"))