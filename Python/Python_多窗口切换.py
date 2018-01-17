from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
searchText = driver.find_element_by_class_name('s_ipt')
searchText.clear()
searchText.send_keys('甄优秀')
searchText.send_keys(Keys.ENTER)

time.sleep(5)

result = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[1]/div[3]/div[1]/h3/a')
result.click()

time.sleep(5)

print(driver.window_handles)

driver.switch_to.active_element(driver.window_handles[1])