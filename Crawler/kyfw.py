#-*- encoding:utf-8 -*-
import urllib,urllib2,requests,ssl
import json,re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class hhSprider:


    def Ticketquery(self,date,start,end):
        ssl._create_default_https_context = ssl._create_unverified_context
        self.url = 'https://kyfw.12306.cn/otn/leftTicket/queryA?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT' %(date,start,end)
        self.headers = {
                    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                    "Accept-Encoding":"gzip, deflate, sdch, br",
                    "Accept-Language":"zh-CN,zh;q=0.8",
                    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
                  }
        self.TicketSession = requests.Session()
        self.TicketSession.headers = self.headers
        self.TicketSession.verify = False

        self.getjson = self.TicketSession.get(self.url)
        print "content ",self.getjson.content
        self.data = json.loads(self.getjson.content)
        print "data ",self.data
        self.left_ticket = self.data['data']
        return self.left_ticket
    def station_name(self,name):
      ssl._create_default_https_context = ssl._create_unverified_context
      js=requests.get('https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8994',verify=False)
      #print js.content.decode('utf-8').encode('mbcs')
      content = js.content#.decode('utf-8').encode('mbcs')

      pattern = re.compile(name+'\|(?P<hh>[A-Z]{3})\|')
      t = re.search(pattern,content)
      if t:
        print t.groups()[0]
      else:
        print 'hh'

      return t.groups()[0]

def main():
    tmp = hhSprider()
    #ss = raw_input('输入出发地'.decode('utf-8').encode('mbcs'))
    #ee = raw_input('输入目的地'.decode('utf-8').encode('mbcs'))
    #tt = raw_input('输入出发日期格式为（2016-09-06）'.decode('utf-8').encode('mbcs'))
    # ss = raw_input('输入出发地')
    # ee = raw_input('输入目的地')
    # tt = raw_input('输入出发日期格式为（2016-09-06）')
    ss='南阳'
    ee='上海'
    tt='2017-02-020'

    start = tmp.station_name(ss)
    end = tmp.station_name(ee)
    res= tmp.Ticketquery(tt,start,end)
    for i in res:
        print '车次:%s' %i['queryLeftNewDTO']['station_train_code'],\
            '   出发时间:%s'%i['queryLeftNewDTO']['start_time'],\
            '   到达时间:%s'%i['queryLeftNewDTO']['arrive_time'],\
            '    一等座：%s'%i['queryLeftNewDTO']['zy_num'],\
            '    二等座：%s'%i['queryLeftNewDTO']['ze_num'],\
            '    软卧：%s'%i['queryLeftNewDTO']['rw_num'],\
            '    硬卧：%s'%i['queryLeftNewDTO']['yw_num'],\
            '    硬座：%s'%i['queryLeftNewDTO']['yz_num'],\
            '    无座：%s'%i['queryLeftNewDTO']['wz_num']





main()