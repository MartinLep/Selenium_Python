from selenium import webdriver

import xlrd

import time

dr=webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')

time.sleep(5)

print('Browser will be closed')

dr.quit()

print('Browser is close')

dr = webdriver.Firefox()
dr.get('https://www.baidu.com')
dr.find_element_by_id('kw').send_keys('123')