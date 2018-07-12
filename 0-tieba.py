# !/usr/bin/env python
# _*_ coding:utf-8 _*_


import urllib2
import urllib


class Tieba_Spider(object):
    def __init__(self):
        # 不同user-agent 可能返回不同数据

        self.base_url = 'http://tieba.baidu.com/f?'
        # self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36"}

    # 发送请求
    def send_request(self, url):
        request = urllib2.Request(url, headers=self.headers)
        response = urllib2.urlopen(request)
        data = response.read()

        return data

    # 保存本地文件
    def write_file(self, data):
        with open('0tieba.html', 'w') as f:
            f.write(data)

    # 调度方法 start_work
    def start_work(self):
        # 贴吧的名字
        # tieba_name = raw_input('请输入抓取的贴吧名字:')
        tieba_name = '美食'

        # 开始的页数
        start_page = 1
        # 结束的页数
        end_page = 1

        # 发送请求
        params = {
            'kw': tieba_name,
            'pn': 0
        }

        # 网址的转译
        params_str = urllib.urlencode(params)
        new_url = self.base_url + params_str
        data = self.send_request(new_url)

        # 保存数据
        self.write_file(data)


if __name__ == '__main__':
    tool = Tieba_Spider()
    tool.start_work()
