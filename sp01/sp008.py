import requests

url = 'http://www.shsxt.com'
proxies = {
    "http": "http://220.191.101.224:6666",
    "https": "http://116.22.55.4:8118",

}
response = requests.get(url,proxies=proxies,timeout=10)
response.encoding='utf-8'
html = response.text
print(html)