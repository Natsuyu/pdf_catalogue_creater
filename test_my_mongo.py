# !/usr/bin/env python
#-*- coding:utf-8 -*-
#
# import requests
#
# url = "http://news-at.zhihu.com/api/4/theme/"
#
# headers = {
#     # 'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
# }
# s = requests.session()
#
# for i in range(15):
#     turl = url + str(i)
#     page = s.get(turl, headers = headers).text
#     print page
# # print src

import sys
d = []
def init():
    j=1
    for i in range(1000010):
       d.append(j*(j+1)*(2*j+1)/6)
       j+=1
# for line in sys.stdin:

    # a = line.split()
h = 10
i = 0
init()
for i in range(1000010):
    if h < d[i]:
        break
print i


