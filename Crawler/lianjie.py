#-*- encoding:utf-8 -*-

from urllib.request import urlopen
from urllib.parse import urlparse
import urllib
from bs4 import BeautifulSoup
import re
import datetime
import random
bestUrl_list = []

pages = set()
random.seed(datetime.datetime.now())
hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
       'Accept-Encoding': 'gzip, deflate, sdch',
       'Accept-Language': 'zh-CN,zh;q=0.8',
       'Connection': 'keep-alive'}

#Retrieves a list of all Internal links found on a page
def getInternalLinks(bsObj, includeUrl):
    includeUrl = urlparse(includeUrl).scheme+"://"+urlparse(includeUrl).netloc
    internalLinks = []
    #Finds all links that begin with a "/"
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if(link.attrs['href'].startswith("/")):
                    print("current internallink is:",link.attrs['href'])
                    internalLinks.append(includeUrl+link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks

def compareLink(pos,li,bestLink):
    if bestLink[li[pos]] not in pages:
        pages.add(bestLink[li[pos]])
        return bestLink[li[pos]]
    elif abs(pos) < len(li):
        compareLink(pos-1,li,bestLink)
    else:
        print ("no link!")
        exit(0)

#Retrieves a list of all external links found on a page
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    bestLink = {}
    #Finds all links that start with "http" or "www" that do
    #not contain the current URL
    for link in bsObj.findAll("a", href=re.compile(
                                "^(http|www)((?!"+excludeUrl+").)*$")):

        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                print("current externlink is:",link.attrs['href'])
                bestLink[countExternalLink(link.attrs['href'])]=link.attrs['href']
                externalLinks.append(link.attrs['href'])

    print ("=======================")
    list1 = list(bestLink.keys())
    list1.sort()
    bestUrl=compareLink(-1,list1,bestLink)
    print ("The best url is:  ",bestUrl)
    #print ("The best url is:  ",bestLink[list1[-1]])
    # if bestLink[list1[-1]] in bestUrl_list:
    #     bestLink[list1[-2]]
    #,bestLink[list(bestLink.keys()).sort()[-1]]
    externalLinks = []
    externalLinks.append(bestUrl)
    return externalLinks


def countExternalLink(Url):
    try:
        html = urlopen(Url)
        bsObj = BeautifulSoup(html, "html.parser")
        excludeUrl = urlparse(Url).netloc
        externalLinks = []
        count = 0
        for link in bsObj.findAll("a", href=re.compile(
                                    "^(http|www)((?!"+excludeUrl+").)*$")):
            if link.attrs['href'] is not None:
                if link.attrs['href'] not in externalLinks:
                    count += 1
        print ("count:  ",count)
    except:
        count = 0
    return count

def getRandomExternalLink(startingPage):
    #req = urllib.request.Request(startingPage, headers=hdr)
    # opener = urllib.request.build_opener()
    # opener.addheaders = [hdr]
    try:
        html = urlopen(startingPage)
        bsObj = BeautifulSoup(html, "html.parser")
        externalLinks = getExternalLinks(bsObj, urlparse(startingPage).netloc)
        print("externalLinks:",externalLinks)
        if len(externalLinks) == 0:
            print("No external links, looking around the site for one")
            domain = urlparse(startingPage).scheme+"://"+urlparse(startingPage).netloc
            internalLinks = getInternalLinks(bsObj, domain)
            if len(internalLinks) == 0: exit(0)
            return getRandomExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
        else:
            print("start recursion...")
            return externalLinks[random.randint(0, len(externalLinks))]
    except:
        exit(0)

def followExternalOnly(startingSite):
    bestUrl_list.append(startingSite)
    externalLink = getRandomExternalLink(startingSite)
    print("Random external link is: ",externalLink)
    print ("=======================")
    followExternalOnly(externalLink)


followExternalOnly("http://xiaorui.cc/")
#http://www.baidu.com/
#http://irory.me/
#http://xiaorui.cc/
#http://oldboy.blog.51cto.com/



