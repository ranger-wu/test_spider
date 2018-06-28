import requests

proxies = {
    'http':'http://218.26.227.108:80',
    'https':'http://27.38.137.229:8118'
}
url = 'http://www.chzu.edu.cn/'
response = requests.get(url=url, proxies=proxies)
html = response.content.decode()
print(html)
