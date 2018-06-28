from selenium import webdriver
from lxml import etree
import time


url = 'https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9' \
      'C%AC&enc=utf-8&wq=%E7%AC%94%E8%AE%B0%E6%9C%AC&pvid=845d019c94f6476ca5c4ffc24df6865a'
driver = webdriver.Chrome()
driver.get(url)
script =  "var q=document.body.scrollTop=0"
driver.execute_script(script)
time.sleep(2)
driver.save_screenshot('jd.png')
print(driver.page_source)
html = driver.page_source
e = etree.HTML(html)
prices = e.xpath('//*[@id="J_goodsList"]/ul/li/div/div[2]/strong/i/text()')
names = e.xpath('//*[@id="J_goodsList"]/ul/li/div/div[3]/a/em')
for p, n in zip(names, prices):
    print(n+':'+p)
print(len(prices))
driver.close()