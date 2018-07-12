# !/usr/bin/env python
# _*_ coding:utf-8 _*_


import urllib2


# 验证是否能用
def verfy_proxy(openner):
    url = 'http://www.baidu.com'
    try:
        response = openner.open(url, timeout=1)
        return response.getcode()
    except urllib2.HTTPError, err:
        return err.code
    except urllib2.URLError, err:
        return 6666


# 筛选 能用的代理IP 池
def can_use_proxy():
    # 1.大量的大理
    proxy_list = [
        {"http": "61.135.217.7:80"},
        {"http": "122.114.31.177:808"},
        {"http": "218.56.237.246:8118"},
        {"http": "106.58.123.187:80"}
    ]

    can_use_list = []
    for proxy in proxy_list:
        handler = urllib2.ProxyHandler(proxy)
        openner = urllib2.build_opener(handler)
        code = verfy_proxy(openner)
        print code
        if (code == 200):
            can_use_list.append(proxy)

    print can_use_list


if __name__ == '__main__':
    can_use_proxy()
