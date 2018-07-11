# !/usr/bin/env python
# _*_ coding:utf-8 _*_


import urllib2


def web_author_data():
    url = 'http://60.205.187.28/login.php'

    # 1.密码管理器
    pwd_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()

    # 添加用户名和密码
    # realm, None
    # uri>url
    # user,\
    # passwd
    pwd_manager.add_password(None, uri=url, user='admin', passwd='admin')

    # 1.handler
    web_handler = urllib2.HTTPBasicAuthHandler(pwd_manager)

    # 2. opener
    openner = urllib2.build_opener(web_handler)

    response = openner.open(url)

    print response.read()

if __name__ == '__main__':
    web_author_data()
