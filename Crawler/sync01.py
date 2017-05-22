__author__ = 'derek'
import requests

r = 100
url = "http://192.168.11.8:8080/{}"
for i in range(r):
    res = requests.get(url.format(i))
    delay = res.headers.get("DELAY")
    d = res.headers.get("DATE")
    print("{}:{} delay {}".format(d, res.url,delay))