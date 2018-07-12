# !/usr/bin/env python
# _*_ coding:utf-8 _*_


import urllib2
import ssl

'''
    urllib2.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:590)>
'''


#  如果 遇到 ssl 认证  告诉系统 忽略认证

def ssl_unverfied():
    # 注意网址
    url = 'https://www.12306.cn/mormhweb/'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    request = urllib2.Request(url, headers=headers)

    # 告诉系统 请求的时候 忽略认证
    context = ssl._create_unverified_context()
    response = urllib2.urlopen(request, context=context)

    data = response.read()

    with open('03ssl.html', 'w') as f:
        f.write(data)


if __name__ == '__main__':
    ssl_unverfied()
