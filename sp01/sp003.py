# <发送get请求获取页面>
import requests

# 爬取的地址:
url = 'http://www.shsxt.com'
# 发送get请求
response = requests.get(url=url)
# 获取响应文本
html = response.content.decode()
print(html)
'''
response.encoding='utf8'
html2 = response.text
print(html2)   #这是用来解决乱码问题!


# <发送post请求页面>
url = 'http://www.shsxt.com'
response = requests.post(url)
html = response.content.decode()
print(html)

'''

