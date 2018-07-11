# !/usr/bin/env python
# _*_ coding:utf-8 _*_


import urllib2


def proxy_handler():
    url = 'http://www.baidu.com'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    request = urllib2.Request(url, headers=headers)

    # 代理IP 对应功能的 处理器
    # proxy = {'协议':'IP:port'}
    # 免费的代理
    # proxy = {'http':'115.223.215.161:9000'}
    proxy = {'http':'175.6.2.174:8088'}
    # proxy = {'http': 'mr_mao_hacker:sffqry9r@120.26.167.140:16816'}

    # 付费的代理
    # money_proxy = {'协议':'username:pwd@IP:port'}

    # 1. 根据功能创建处理器
    proxy_hander = urllib2.ProxyHandler(proxy)

    # 2. 根据处理器生成openner
    openner = urllib2.build_opener(proxy_hander)

    # 3. open 发送请求
    response = openner.open(request)

    print response.read()


if __name__ == '__main__':
    proxy_handler()
