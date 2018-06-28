# 导包
from http.cookiejar import CookieJar
from urllib.request import HTTPCookieProcessor
from urllib.request import build_opener
from urllib.request import Request
# from urllib.parse import urlencode


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
cookjar = CookieJar()
pro = HTTPCookieProcessor(cookjar)
opener = build_opener(pro)
url = ('https://dig.chouti.com')
request = Request(url, headers=headers)
response = opener.open(request)
new_url = ('https://dig.chouti.com/link/20159466')
new_request = Request(new_url, headers=headers)
new_response = opener.open(new_request)
print(new_response.read().decode())
