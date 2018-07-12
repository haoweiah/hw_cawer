# !/usr/bin/env python
# _*_ coding:utf-8 _*_


import urllib2


# 自定openner的原因: 系统自带的urlopen是没有 代理IP,web认证,cookie携带功能

def custom_handler_openner():
    url = 'http://www.baidu.com'
    # 'http://www.gatherproxy.com/zh/'

    # 1.处理器
    handler = urllib2.HTTPHandler(debuglevel=1)

    # 2. openner
    openner = urllib2.build_opener(handler)

    # 3.openner.open 发送请求
    response = openner.open(url)

    # print response.read()


if __name__ == '__main__':
    custom_handler_openner()
