# !/usr/bin/env python
# _*_ coding:utf-8 _*_


import urllib2


class Douban_Spider(object):
    def __init__(self):
        self.base_url = 'https://movie.douban.com/typerank?type_name=%E5%8A%A8%E4%BD%9C&type=5&interval_id=100:90&action='
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 发送请求
    def send_request(self):
        request = urllib2.Request(self.base_url, headers=self.headers)
        response = urllib2.urlopen(request)
        data = response.read()
        return data

    # 写入本地文件
    def write_file(self, data):
        with open('01-douban.html', 'w') as f:
            f.write(data)

    # 调度的方法
    def start_work(self):
        # 发送请求
        data = self.send_request()
        # 保存
        self.write_file(data)


if __name__ == '__main__':
    tool = Douban_Spider()
    tool.start_work()
