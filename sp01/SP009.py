import requests

url = 'http://www.12306.cn'

response = requests.get(url)
response.encoding = 'utf-8'
html = response.text
print(html)
# print(html)

