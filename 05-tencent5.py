# !/usr/bin/env python
# _*_ coding:utf-8 _*_


import requests
from bs4 import BeautifulSoup
from lxml import etree
import json
import time


class Tencen_Spider(object):
    def __init__(self):
        self.base_url = 'https://hr.tencent.com/position.php?'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

        # 将每一行的数据 放入list
        self.item_list = []

        self.page = 0

    # 发送请求
    def send_request(self, url, params={}):
        time.sleep(1)
        try:
            data = requests.get(url, params=params, headers=self.headers).content
            return data
        except Exception, err:
            print err

    # 数据解析
    def analysis_data(self, data):
        # 1.转换类型
        soup = BeautifulSoup(data, 'lxml')

        # 2.解析
        # 2.1 取出 每一行的 tr标签 list
        tr_list = soup.select('.even,.odd')

        # 2.2 再取出 目标的标签 td
        for tr in tr_list:
            item_dict = {}
            # 职位名称
            item_dict['work_name'] = tr.select('td a')[0].get_text()
            # 职位类别
            item_dict['work_type'] = tr.select('td')[1].get_text()
            # 人数
            item_dict['work_count'] = tr.select('td')[2].get_text()
            # 地点
            item_dict['work_place'] = tr.select('td')[3].get_text()
            # 发布时间
            item_dict['work_time'] = tr.select('td')[4].get_text()

            self.item_list.append(item_dict)

        # 返回 最大的页数 找到标签 文本
        big_element = soup.select('.pagenav a')[-2].get_text()

        return big_element

    # 写入本地文件
    def write_file(self):
        # 将list  转换成  str
        # data_str = json.dumps(self.item_list)
        # with open('05tencent.json', 'w') as f:
        #     f.write(data_str)

        json.dump(self.item_list, open('05-tencent5.json', 'w'))

    # 调度
    def start_work(self):

            # 1.拼接参数
            params = {
                "keywords": "python",
                "lid": "2175",
                "tid": "0",
                "start": 0,
            }

            # 2.发送请求
            data = self.send_request(self.base_url, params=params)
            # 3.解析 获取 最大的页数
            big_number = self.analysis_data(data)

            # 根据 最大的页数 开启循环
            for page in range(10, int(big_number) * 10, 10):
                # 1.拼接参数
                params = {
                    "keywords": "python",
                    "lid": "2175",
                    "tid": "0",
                    "start": page,
                }
                print page

                # 2.发送请求
                data = self.send_request(self.base_url, params=params)
                # 3.解析
                self.analysis_data(data)



            # 4. 存html .json
            self.write_file()


if __name__ == '__main__':
    tool = Tencen_Spider()
    tool.start_work()
