# !/usr/bin/env python
# _*_ coding:utf-8 _*_


from selenium import webdriver


if __name__ == '__main__':

    url = "http://www.so.com"

    driver = webdriver.PhantomJS()

    driver.get(url)

    # 修改 文本框的 框子 红色
    str_js = " var element = document.getElementById('input'); element.style.border = '1px solid red';"

    driver.execute_script(str_js)

    driver.save_screenshot("05so.png")