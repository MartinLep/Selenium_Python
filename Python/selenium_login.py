from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium_log import Loginloginfo, XLLoginfo
from selenuim_loginData import get_loginfo, get_loginuserdata , XLUserInfo

class LoginTest(object):

    def __init__ (self, selenium_driver, url, parent=None):
        self.base_url = url
        self.driver = selenium_driver
        self.timeOut = 30
        self.parent = parent
        self.tabs = {}

    def _open(self):
        print(self.base_url)
        self.driver.get(self.base_url)
        # assert self.on_page(), 'Did not land on %s' % self.base_url

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def open(self):
        self._open(self.url)

    def script(self, src):
        return self.driver.execute_script(src)

    def on_page(self):
        print(self.driver.current_url)

    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            loc = getattr(self, '_%s' % loc)
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError:
            print('%s page does not have "%s" locator' % (self, loc))


class LoginPageTest(LoginTest):

    def open(self):
        self._open()

    def type_getlogbtn(self, ele1, ele2):
        element = ele1
        self.find_element(*(By.XPATH, ele1)).click()
        self.find_element(*(By.XPATH, ele2)).click()

    def type_username(self, ele, userName):
        self.find_element(*(By.XPATH, ele)).send_keys(userName)

    def type_password(self, ele, passWord):
        self.find_element(*(By.XPATH, ele)).send_keys(passWord)

    def submit(self, ele):
        self.find_element(*(By.XPATH, ele)).click()

def test_user_login(driver, loginfo, userdata):
    login_page = LoginPageTest(driver,userdata['url'])
    login_page.open()
    login_page.type_getlogbtn(loginfo['loginBtn'], loginfo['logfunc'])
    login_page.type_username(loginfo['userName_loc'], userdata['username'])
    login_page.type_password(loginfo['passWord_loc'], userdata['password'])
    login_page.submit(loginfo['submit_loc'])

def checkResult(driver, elementid, datadic, xlloginfo):
    reslut = False
    try:
        print(elementid)
        ele = driver.find_element_by_class_name(elementid)
        msg = 'uname=%s pwd=%s:error:%s\n' % (datadic['username'], datadic['password'], ele.text)
        xlloginfo.XL_Write(datadic['username'], datadic['password'], 'Error', ele.text)
        print('error = ',msg)
    except:
        msg = 'uname=%s pwd=%s:pass\n'%(datadic['username'],datadic['password'])
        xlloginfo.XL_Write(datadic['username'], datadic['password'], 'Pass')
        print(msg)
        reslut = True
    return reslut

def logout(driver, elementid):
    driver.find_element_by_xpath(elementid).click()

def main():
    try:
        driver = webdriver.Firefox()
        driver.maximize_window()
        # url = 'http://www.yiuxiu.com'
        # username = '15380516579'
        # password = '123456'
        loginfo = get_loginfo(r'F:\selenium_Python\Python\loginfo')

        # userdatabase = get_loginuserdata(r'F:\selenium_Python\Python\loguserdata')
        xinfo = XLUserInfo(r'F:\selenium_Python\Python\DataDocument\LoginUserData.xlsx')
        userdatabase = xinfo.get_sheetinfo_by_index(0)
        print(userdatabase)
        xlloginfo = XLLoginfo()
        xlloginfo.XL_init('Sheet1','uname', 'pwd', 'result', 'msg')
        for datadic in userdatabase:
            print(datadic)
            test_user_login(driver, loginfo, datadic)
            result = checkResult(driver, loginfo['errorid'], datadic, xlloginfo)
            if result:
                logout(driver, loginfo['logout'])

        print('logfile.log_closed')
        logfile.XL_Close()

    finally:
        print('nihao')
        # driver.close()

if  __name__ == '__main__':
    main()