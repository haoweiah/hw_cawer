# !/usr/bin/env python
# _*_ coding:utf-8 _*_

from selenium import webdriver
import time

def base_use_selenium():
    url = 'https://www.so.com/'

    # 1.创建浏览器对象
    driver = webdriver.PhantomJS()

    # 2.请求数据
    driver.get(url)
    time.sleep(2)
    # 4.数据 unicode-->str
    # data = driver.page_source
    # print type(data.encode('utf-8'))
    # print data

    # 5. 点击 新闻按钮
    element = driver.find_element_by_xpath('//*[@id="bd_tabnav"]/nav/a[2]')
    element.click()
    # print element

    time.sleep(2)
    # 6. 给 输入框 输入内容 --写 unicode
    driver.find_element_by_id('haosou-input').send_keys(u'赵薇')

    time.sleep(2)
    # 7. 点击 放大镜的 按钮 搜索
    driver.find_element_by_xpath('//*[@id="search-form"]/div/button').click()
    #
    # 8.获取当前的 页面 0,1
    print driver.window_handles

    # 9.切换 页面 1
    driver.switch_to_window(driver.window_handles[1])

    # 3.保存快照
    driver.save_screenshot('1so.png')

    # driver.get_cookies()
    # driver.current_url

    # 关闭浏览器
    driver.quit()

    print "over......"


if __name__ == '__main__':
    base_use_selenium()
