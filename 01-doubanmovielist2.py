# !/usr/bin/env python
# _*_ coding:utf-8 _*_


import urllib2
import urllib

#  ajax 动态加载数据: 你需要找到正确 的网址
#   将来我们获取的数据 绝大多数都是ajax
class Douban_Spider(object):
    def __init__(self):
        self.base_url = 'https://movie.douban.com/j/chart/top_list?'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 发送请求
    def send_request(self, url):
        request = urllib2.Request(url, headers=self.headers)
        response = urllib2.urlopen(request)
        data = response.read()
        return data

    # 写入本地文件
    def write_file(self, data):
        with open('01-douban.json', 'w') as f:
            f.write(data)

    # 调度的方法
    def start_work(self):
        # 拼接参数
        params = {
            "type": "5",
            "interval_id": "100:90",
            "action": "",
            "start": "20",
            "limit": "20",
        }

        # url 转译
        params_str = urllib.urlencode(params)
        url = self.base_url + params_str
        print url
        # 发送请求
        data = self.send_request(url)
        # 保存
        self.write_file(data)


if __name__ == '__main__':
    tool = Douban_Spider()
    tool.start_work()
