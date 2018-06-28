
# <过滤器>
from bs4 import BeautifulSoup
import re
html = '''
<title>尚学堂</title>
<div class='info' float='left'>Welcome to SXT</div>
<div class='info' float='right'>
<span>Good Good Study</span>
<a href='www.bjsxt.cn'></a>
<strong><!-- 没用 --></strong>
</div> '''
soup = BeautifulSoup(html, 'lxml')
#print(soup.find_all('div'))  以列表形式打印所有div标签
#print(soup.find_all('strong'))
#print(soup.find_all(re.compile('^a')))  #以正则形式打印所有a标签,结果以列表形式返回
#print(soup.find_all(['span','a']))  #传入列表参数
#print(soup.find_all(id='welcom'))    结果: []
#print(soup.find_all('div',attrs={'class':'info'}))
#print(soup.find_all('div',class_='info'))
