# ActionChains 类提供的鼠标操作的常用方法：
# 1. context_click() 右击
# 2. double_click() 双击
# 3. drag_and_drop() 拖动
# 4. move_to_element() 鼠标悬停
# 5. perform() 执行所有 ActionChains 中存储的行为

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

def log_test():
    driver = webdriver.Firefox()

    driver.get('http://www.yiuxiu.com')
    logEle = driver.find_element_by_class_name('po-r')
    ActionChains(driver).move_to_element(logEle).perform()
    # ActionChains(driver).context_click(logEle).perform()
    logBtn = driver.find_element_by_xpath('/html/body/div[1]/div/ul[2]/li[1]/div/div[2]/a')
    logBtn.click()

    logEleBtn = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/ul/li[2]')
    logEleBtn.click()

    from selenium.webdriver.common.keys import Keys
    phoneText = driver.find_element_by_class_name('username')
    phoneText.send_keys('18658196789')
    time.sleep(2)
    phoneText.send_keys(Keys.BACK_SPACE)
    time.sleep(2)
    phoneText.send_keys(Keys.CONTROL, 'a')
    time.sleep(2)
    phoneText.send_keys(Keys.CONTROL, 'x')
    time.sleep(2)
    phoneText.send_keys(Keys.CONTROL, 'v')
    time.sleep(2)

    driver.find_element_by_class_name('password').send_keys('123456')

    driver.find_element_by_class_name('password').send_keys(Keys.ENTER)

    try:
        e_error = driver.find_element_by_class_name('wrong-notice')
        print('Account error')
    except:
        print('login success')
        # 也可定位登陆按钮，通过enter（回车）代替click()
        # driver.find_element_by_class_name('login-btn').click()


if __name__ == '__main__':
    log_test()