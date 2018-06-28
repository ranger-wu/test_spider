#  伪装浏览器,携带报头
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/'
                  '537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
url = 'http://www.chzu.edu.cn/'
response =requests.get(url,headers=headers)
response.encoding='utf8'
html = response.text
print(html)