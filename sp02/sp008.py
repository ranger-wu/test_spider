from selenium import webdriver
from lxml import etree
import time
# 目标地址
url = 'https://list.jd.com/list.html?cat=9987,653,655'
# driver驱动
driver = webdriver.Chrome()
# driver获取页面支持
driver.get(url)
# 找到滚动条
script = 'var q=document.body.scrollTop=0'
# dirver执行脚本
driver.execute_script(script)
# 设定延时等待,获取页面资源
time.sleep(3)
print(driver.page_source)
html = driver.page_source
# 通过获取的页面构建树状结构!
e = etree.HTML(html)
# 利用xpath 解析树
price = e.xpath('//*[@id="plist"]/ul/li/div/div[3]/strong')
name = e.xpath('//*[@id="J_crumbsBar"]/div/div/div/div[1]/a')
print(price, len(price))
print(name, len(name))
#driver.close()