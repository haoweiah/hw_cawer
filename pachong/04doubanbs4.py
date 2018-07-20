# !/usr/bin/env python
# _*_ coding:utf-8 _*_


import requests
from bs4 import BeautifulSoup
from lxml import etree


def douba_data():
    url = 'https://movie.douban.com/cinema/nowplaying/shanghai/'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    data = requests.get(url, headers=headers).content

    #  验证数据的正确性

    # 1. bs4
    # 1.1 转换类型
    soup = BeautifulSoup(data, 'lxml')

    # 1.2 select--list
    result = soup.select('#7056414 .stitle a')[0].get_text().strip()

    # 2.xpath
    # 2.1 转换解析的类型
    html_data = etree.HTML(data)

    # 2.2 解析 --list
    result = html_data.xpath('//*[@id="7056414"]/ul/li[2]/a/text()')[0].strip()

    print result


if __name__ == '__main__':
    douba_data()
