import time
from selenium import webdriver

from lxml import etree

browser = webdriver.Chrome()

browser.get(
    'https://search.jd.com/Search?keyword=%E5%8D%8E%E7%A1%95&enc=utf-8&wq=%E5%8D%8E%E7%A1%95&pvid=9cf18cd745dc4274bb6d4a7ef03ee6a4')

data = []


def test():
    global data
    product = {}
    sales = browser.find_element_by_xpath('//*[@id="J_filter"]/div[1]/div[1]/a[2]/span')
    sales.click()

    for item in range(10):
        js = "var q=document.documentElement.scrollTop={}".format(1000 * (item + 1))
        browser.execute_script(js)
        time.sleep(0.5)

    html = browser.page_source

    html = etree.HTML(html)
    divs = html.xpath('//*[@id="J_goodsList"]/ul/li/div')

    for div in divs:
        title = div.xpath('./div[@class="p-name p-name-type-2"]/a/i/text()')
        if title:
            product['title'] = title[0]
            continue
        product['title'] = ''

    for div in divs:
        price = div.xpath('./div/strong/i/text()')
        product['price'] = price

    data.append(product)


for item in range(4):
    nextpage = browser.find_element_by_xpath('//*[@id="J_bottomPage"]/span[1]/a[9]')
    nextpage.click()
    test()

print(len(data))
