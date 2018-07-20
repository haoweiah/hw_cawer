# !/usr/bin/env python
# _*_ coding:utf-8 _*_


import urllib.request
import


def cookjar_handler():
    # 1.创建 cookjar 就是用来保存cookie的
    cookjar = cookielib.CookieJar()

    # 2. 创建有cookie功能的处理器
    handler = urllib.request.HTTPCookieProcessor(cookjar)

    # 3. 根据处理器 生成openner
    openner = urllib2.build_opener(handler)

    # 1.代码登录
    login_url = 'http://www.renren.com/PLogin.do'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # post 用户名和密码
    formdata = {
        "email": "mr_mao_hacker@163.com",
        "password": "alarmchime"
    }
    formdata_str = urllib.urlencode(formdata)

    # 发送登录的请求 openner
    login_request = urllib2.Request(login_url, data=formdata_str, headers=headers)
    openner.open(login_request)

    # 2.如果是成功的 需要成功之后的cookie
    # 3. 带着有效的cookie 访问好有页面 拿到数据
    profile_url = 'http://www.renren.com/410043129/profile'
    profile_request = urllib2.Request(profile_url, headers=headers)

    try:
        response = openner.open(profile_request)
        data = response.read()

        with open('07renren.html', 'w') as f:
            f.write(data)

    except Exception as err:
        print(err)




if __name__ == '__main__':
    cookjar_handler()
