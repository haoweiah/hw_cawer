# !/usr/bin/env python
# _*_ coding:utf-8 _*_


import json
import csv

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def json_to_csv_dat():

    # 1.json文件 读取
    json_file = open('05-tencent5.json', 'r')
    # 2.csv文件  写入
    csv_file = open('06csv.csv', 'w')
    # 3.csv的读写器
    csv_writer = csv.writer(csv_file)

    # 转换成 python list
    data_list = json.load(json_file)

    #3.取出表头
    sheets = data_list[0].keys()

    #4.取出内容
    content_list = []
    for data_dict in data_list:
        content_list.append(data_dict.values())

    # 5.写入 表头
    csv_writer.writerow(sheets)
    # 6.写入 内容
    csv_writer.writerows(content_list)

    # 7.关闭csv
    csv_file.close()
    # 8.关闭json
    json_file.close()


if __name__ == '__main__':
    json_to_csv_dat()