# encoding:utf-8
from selenium import webdriver
import time

def base_use_selenium():
    driver = webdriver.Chrome()
    base_url = 'https://www.github.com'
    login_url = base_url +'/login'
    driver.get(login_url)
    driver.find_element_by_id('login_field').send_keys(u'hw121298@163.com')
    driver.find_element_by_id('password').send_keys('!QAZ2wsx')
    driver.find_element_by_name('commit').click()
    driver.get(base_url+'/jianlaipinan/carn/pull/8')
    driver.find_element_by_xpath('//*[@id="partial-pull-merging"]/div[1]/div/div/div/div[3]/div[1]/div[1]/button[1]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="partial-pull-merging"]/div[1]/form/div/div[2]/div/div[1]/button').click()
    driver.save_screenshot('bd.png')
    driver.quit()
    print('over....')

if __name__ == '__main__':
    base_use_selenium()