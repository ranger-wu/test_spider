import requests

cookies = {
    'cookie': '1234'
    }
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/'
                  '537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
url = 'https://www.itbaizhan.cn/dashboard.html'
response = requests.get(url=url, cookies=cookies)
html = response.content.decode()
print(html)