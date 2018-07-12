# !/usr/bin/env python
# _*_ coding:utf-8 _*_


from selenium import webdriver
import time

def login_douban():

    # 1.登录的网址
    url = 'https://www.douban.com/accounts/login?source=movie'

    # 2.创建浏览器对象
    driver = webdriver.PhantomJS()

    # 3.请求url
    driver.get(url)

    # 4.用户名
    driver.find_element_by_id('email').send_keys(u"mr.mao.tony@gmail.com")
    # 5.密码
    driver.find_element_by_id('password').send_keys(u'ALARMCHIME')

    driver.find_element_by_name('login').click()
    time.sleep(2)

    # 保存快照 查看验证码 手动输入
    driver.save_screenshot('02code.png')
    code = raw_input("请输入验证码:")
    # 验证码
    driver.find_element_by_id('captcha_field').send_keys(code)

    # 6. 点击登录按钮
    driver.find_element_by_name('login').click()


    driver.save_screenshot("02douban.png")
if __name__ == '__main__':
    login_douban()
