# !/usr/bin/env python
# _*_ coding:utf-8 _*_


from selenium import webdriver
from bs4 import BeautifulSoup
import time


class Douyu_Spider(object):
    def __init__(self):
        self.base_url = 'https://www.douyu.com/directory/all'
        self.driver = webdriver.PhantomJS()
        self.count = 0

    def send_reqeust(self):
        # 发送请求
        self.driver.get(self.base_url)
        data = self.driver.page_source
        return data

    # 解析数据
    def analysis_data(self, data):
        # 1.转换类型
        soup = BeautifulSoup(data, 'lxml')

        # 2.解析数据
        # 2.1 取出当前的 ul
        ul_element = soup.select('#live-list-contentbox')[0]

        # 2.2 房间名字
        room_list = ul_element.select('.ellipsis')
        # 2.3 主播名字
        name_list = ul_element.select('.dy-name')
        # 2.4 热度
        hot_list = ul_element.select('.dy-num')

        for room, name, hot in zip(room_list, name_list, hot_list):
            print room.get_text().strip()
            print name.get_text()
            print hot.get_text()
            self.count += 1

        return soup

    def start_work(self):
        data = self.send_reqeust()
        soup = self.analysis_data(data)

        while True:

            # 延迟 3秒钟 保证浏览器 渲染完毕
            time.sleep(3)

            # 判断 下一页 不能点击的 属性 在不在
            if data.find('shark-pager-disable-next') != -1:
                break

            # 1.获取 下一页的 按钮
            next_element = self.driver.find_element_by_class_name("shark-pager-next")

            # 2.click
            next_element.click()

            data = self.driver.page_source
            self.analysis_data(data)

        print self.count

        # 关闭浏览器
        self.driver.quit()


        # list1 = ["a", "b", "c"]
        # list2 = ["A", "B", "C"]
        # list3 = ["100", "200", "300"]
        #
        # list4 = zip(list1, list2, list3)
        # print list4


if __name__ == '__main__':
    tool = Douyu_Spider()
    tool.start_work()
