# !/usr/bin/env python
# _*_ coding:utf-8 _*_


import requests
from bs4 import BeautifulSoup
import json


class Tencen_Spider(object):
    def __init__(self):
        self.base_url = 'https://www.qiushibaike.com/8hr/page/'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.item_list = []


    # 发送请求
    def send_request(self, url):
        try:
            data = requests.get(url, headers=self.headers).content

            # print data
            return data
        except Exception, err:
            print err

    # 数据解析
    def analysis_data(self, data):

        soup = BeautifulSoup(data, 'lxml')

        #  先取出 所有的 子的div---list
        children_div_list = soup.select('#content-left .article')

        # 循环取出 我们需要的数据
        for content in children_div_list:
            item_dict = {}
            # 1.昵称
            item_dict['nick_name'] = content.select('.author h2')[0].get_text().strip()
            # 4.正文
            item_dict['detail_content'] = content.select('.content span')[0].get_text().strip()
            # 5.点赞数
            item_dict['number'] = content.select('.number')[0].get_text()

            # 2.年龄
            div_element = content.select('.articleGender')
            if div_element:
                # 注意点 class 取出来list articleGender manIcon
                item_dict['age'] = content.select('.articleGender')[0].get_text()

                # 3.性别
                item_dict['gender'] = content.select('.articleGender')[0].get('class')[1].replace("Icon", "")
            else:
                item_dict['age'] = '无'
                item_dict['gender'] = '无'

            self.item_list.append(item_dict)


    # 写入本地文件
    def write_file(self):
        json.dump(self.item_list, open('07qiushi.json', 'w'))

    # 调度
    def start_work(self):

        for page in range(1,5):
            url = self.base_url + str(page)
            # 2.发送请求
            data = self.send_request(url)

            # 3.解析
            self.analysis_data(data)
        # 4. 存html .json
        self.write_file()



if __name__ == '__main__':
    tool = Tencen_Spider()
    tool.start_work()
