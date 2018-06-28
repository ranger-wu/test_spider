import json
import jsonpath
import requests

headers = {
    'authorization': '17506481184@w12345678',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'  # 此处填写你自己浏览器的User-Agent
}
# 爬取页面
url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json'
response = requests.get(url, headers=headers)
html = response.text

# 解析页面:
# ①加载html
js = json.loads(html)

# ②获取城市名:利用jsonpath
'''
city = jsonpath.jsonpath(js, '$..name')
print(city)

city = jsonpath.jsonpath(js, '$..A..name')
print(city)

code = jsonpath.jsonpath(js, '$..code')
print(code)
'''
citys = jsonpath.jsonpath(js, '$..A..name')
codes = jsonpath.jsonpath(js, '$..A..code')
for city,code in zip(citys,codes):
    print(code+':'+city)