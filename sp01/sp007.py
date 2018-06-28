import requests

url = "http://www.baidu.com/s"
params = {'wd': '滁州学院'}
response = requests.get(url, params=params)
print(response.url)
response.encoding = 'utf-8'
html = response.text

# 这里注意:resp.text 获取的响应内容:是以字符串/  /   resp.conten则是以字节形式
# 这里{'wd':"滁州学院"}表示要搜索的关键信息是:滁州学院, 打开连接后会发现URL中的[wd]
# https://www.baidu.com/s?wd=%E6%BB%81%E5%B7%9E%E5%AD%A6%E9%99%A2
# timeout 设置超时
