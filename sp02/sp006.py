from selenium import webdriver
from lxml import etree
import time

url = 'https://list.jd.com/list.html?cat=670%2C671%2C672&go=0'
driver = webdriver.Chrome
driver.get(url)
num = driver.find_element_by_xpath('//*[@id="J_filter"]/div[1]/div[1]/a[1]')
num.clicke()
js = "document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(3)
e = etree.HTML(driver.page_source)
price = e.xpath('//*[@id="plist"]/ul/li/div/div[2]/strong')
name = e.xpath('//*[@id="plist"]/ul/li/div/div/a/em/text()')

