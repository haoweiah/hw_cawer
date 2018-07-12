# !/usr/bin/env python
# _*_ coding:utf-8 _*_


import urllib2

def error_data():

    url = 'http://www.itcast.cn/fadsfdsfds.txt'

    try:
         response = urllib2.urlopen(url,timeout=2)
    except urllib2.HTTPError,err:
        print err.code

    except urllib2.URLError,err:
        print err



if __name__ == '__main__':
    error_data()