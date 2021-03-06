# -*- coding: utf-8 -*-
import scrapy
import sys
import io
from scrapy.http import Request
from scrapy.selector import Selector, HtmlXPathSelector
from ..items import ChoutiItem


sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

class ChoutiSpider(scrapy.Spider):
    name = "chouti"
    allowed_domains = ["chouti.com"]
    start_urls = ['http://dig.chouti.com/']

    visited_urls =set()
    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield Request(url,callback=self.parse)

    def parse(self, response):
        # content = str(response.body,encoding='utf-8')
        # 找到文档中所有A标签
        # hxs = Selector(response=response).xpath('//a') # 标签对象列表
        # for i in hxs:
        #     print(i) # 标签对象

        # 对象转换为字符串
        # hxs = Selector(response=response).xpath('//div[@id="content-list"]/div[@class="item"]').extract()  # 标签对象列表
        # hxs = Selector(response=response).xpath('//div[@id="content-list"]/div[@class="item"]')  # 标签对象列表
        # for obj in hxs:
        #     a = obj.xpath('.//a[@class="show-content"]/text()').extract_first()
        #     print(a.strip())
        # 选择器：
        """
        //   表示子孙中
        .//  当前对象的子孙中
        /    儿子
        /div 儿子中的div标签
        /div[@id="i1"]  儿子中的div标签且id=i1
        /div[@id="i1"]  儿子中的div标签且id=i1
        obj.extract()         # 列表中的每一个对象转换字符串 =》 []
        obj.extract_first()   # 列表中的每一个对象转换字符串 => 列表第一个元素
        //div/text()    获取某个标签的文本

       """

        # 获取当前页的所有页码

        # hxs = Selector(response=response).xpath('//div[@id="dig_lcpage"]//a/text()')
        # hxs = Selector(response=response).xpath('//div[@id="dig_lcpage"]//a/@href').extract()
        # hxs = Selector(response=response).xpath('//a[starts-with(@href, "/all/hot/recent/")]/@href').extract()

        # response
        hxs1 = Selector(response=response).xpath('//div[@id="content-list"]/div[@class="item"]')  # 标签对象列表
        for obj in hxs1:
            title = obj.xpath('.//a[@class="show-content"]/text()').extract_first().strip()
            href =  obj.xpath('.//a[@class="show-content"]/@href').extract_first().strip()
            item_obj = ChoutiItem(title=title,href=href)

            # 将item对象传递给pipeline
            yield item_obj


        hxs2 = Selector(response=response).xpath('//a[re:test(@href, "/all/hot/recent/\d+")]/@href').extract()
        for url in hxs2:
            md5_url = self.md5(url)
            if md5_url in self.visited_urls:
                pass
            else:
                self.visited_urls.add(md5_url)
                url = "http://dig.chouti.com%s" %url
                # 将新要访问的url添加到调度器
                yield Request(url=url,callback=self.parse)
        # a/@href  获取属性
        # //a[starts-with(@href, "/all/hot/recent/")]/@href'  已xx开始
        # //a[re:test(@href, "/all/hot/recent/\d+")]          正则
        # yield Request(url=url,callback=self.parse)          # 将新要访问的url添加到调度器
        # 重写start_requests，指定最开始处理请求的方法

    # def show(self,response):
    #     print(response.text)

    def md5(self,url):
        import hashlib
        obj = hashlib.md5()
        obj.update(bytes(url,encoding='utf-8'))
        return obj.hexdigest()












