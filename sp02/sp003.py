# 页面交互操作:利用爬虫操作登录网页!
# 导包
from selenium import webdriver
import time
# from bs4 import BeautifulSoup

#选择浏览器
driver = webdriver.Chrome()
#登录目标地址
driver.get("http://www.sxt.cn")
# 让操作等待2秒
time.sleep(2)
# 模拟点击登录
driver.find_element_by_link_text('登录').click()
time.sleep(2)
# 这里输入网页缓存的账号跟密码
driver.find_element_by_name('account').send_keys('17506481184')
time.sleep(2)
driver.find_element_by_name('password').send_keys('12345678')
time.sleep(2)
cookie = driver.get_cookies()
time.sleep(3)
driver.get('https://http://www.sxt.cn')
time.sleep(5)


def execute_times(times):
    for i in range(times + 1):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
execute_times(10)