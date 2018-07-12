# !/usr/bin/env python
# _*_ coding:utf-8 _*_


import requests


def requests_base_use():
    url = 'http://www.baidu.com'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 1.get 自动转码 url的转译
    params = {}
    response = requests.get(url, params=params, headers=headers)

    print type(response.text) # unicode
    print type(response.content) # str

    # 2.post
    formdata = {}
    response = requests.post(url, data=formdata, headers=headers)

    # 3.ssl
    response = requests.get(url, verify=False)

    # 4.proxy
    proxy = {}
    response = requests.get(url, proxies=proxy)

    # 5.cookie
    session = requests.session()
    # 通过session发送的请求 可以自动记录cookie
    session.post(url, data={})

    # 用自带的cookie 发送数据请求的url
    session.get(url)

    # 6.webauth 了解
    auth = ('username', 'pwd')
    requests.get(url, auth=auth)


if __name__ == '__main__':
    requests_base_use()
