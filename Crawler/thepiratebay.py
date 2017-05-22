#-*- encoding:utf-8 -*-
__author__ = 'Aladin'

# coding= utf-8
import urllib2
import re
import pymongo
import ssl
import httplib



#db = pymongo.Connection().test
client = pymongo.MongoClient('localhost',27017)
db = client.test

#context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)

# hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
#        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
#        'Accept-Encoding': 'none',
#        'Accept-Language': 'pl-PL,pl;q=0.8',
#        'Connection': 'keep-alive'}

hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
      # 'cookie':'cfduid=da4e27c16f472483046aca159f8b617701481625665; PHPSESSID=2401ac98ed7a0417005ab9b17d5dfb88; language=zh_CN; tpbpop=1%7CTue%2C%2013%20Dec%202016%2022%3A41%3A22%20GMT',
       'Accept-Language': 'en,zh-CN,cn;q=0.8',
       'Connection': 'keep-alive'}

url = 'https://thepiratebay.org/browse/200/%d/3'

find_re = re.compile(r'<tr>.+?\(.+?">(.+?)</a>.+?class="detLink".+?">(.+?)</a>.+?<a href="(magnet:.+?)" .+?Uploaded (.+?), Size (.+?),', re.DOTALL)

# 定向爬去10页最新的视频资源
for i in range(0, 10):
    u = url % (i)
    # 下载数据
    print "The %s page" % (i+1)
    req = urllib2.Request(u, headers=hdr)
    html = urllib2.urlopen(req).read()
    #print html
    # 找到资源信息
    for x in find_re.findall(html):
        values = dict(
            category = x[0],
            name = x[1],
            magnet = x[2],
            time = x[3],
            size = x[4]
        )
        #  print  'category', '\t', x[0]
        #  print   'name', '\t', x[1]
        #  print   'magnet', '\t', x[2]
        #  print   'time', '\t', x[3]
        #  print   'size', '\t', x[4]
        # 保存到数据库
        db.priate.save(values)

print 'Done!'
