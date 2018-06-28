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
print(soup.select('.class'))