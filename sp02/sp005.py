from selenium import webdriver
from lxml import etree
import time

url = 'https://list.jd.com/list.html?cat=670%2C671%2C672&go=0'

wd = webdriver.Chrome()
wd.get(url)
js = "var q = document.documentElement.scrollTop=10000"
wd.execute_script(js)
time.sleep(3)
e = etree.HTML(wd.page_source)
# 提取数据的 xpath
prices = e.xpath('//*[@id="J_goodsList"]/ul/li/div/div[2]/strong/i/text()')
names = e.xpath('//*[@id="J_goodsList"]/ul/li/div/div[3]/a/em')
