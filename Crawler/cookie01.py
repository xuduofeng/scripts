__author__ = 'derek'

import http.cookiejar
import urllib.request

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print ('Name = ' + item.name)
    print ('Value = ' + item.value)
