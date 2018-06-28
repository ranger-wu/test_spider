from http.cookiejar import CookieJar
from urllib.request import HTTPCookieProcessor
from urllib.request import build_opener
from urllib.request import Request ,urlopen
import ssl

#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
url = 'https://dig.chouti.com'
request = Request(url)

response = urlopen(request,context=context)
print()
