#import requests
from bs4 import BeautifulSoup

html = '''
<title>尚学堂</title>
<div class='info' float='left'>Welcome to SXT</div>
<div class='info' float='right'>
<span>Good Good Study</span>
<a href='www.bjsxt.cn'></a>
<strong><!-- 没用 --></strong>
</div> '''
soup = BeautifulSoup(html, 'lxml')
# print(soup)
# print(soup.title)    #结果:<title>尚学堂</title>
# print(soup.div)     #两个标签中,默认打印的是第一个div
# print(soup.div.attrs)   #打印的是标签中的属性
# print(soup.div.get('float'))  #打印属性的值
# print(soup.div['class'])  #打印属性的值
# print(soup.title.string)
# print(soup.div.string)  打印标签的文本
# print(soup.title.text)   打印标签的文本
