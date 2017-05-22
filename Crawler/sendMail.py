__author__ = 'derek'
#-*-coding:utf-8-*-
import smtplib
from email.mime.text import MIMEText

msg = MIMEText("测试")
msg['Subject'] = "An Email Alert"
msg['From'] = 'chengjianfeng@huiti.com'
msg['']
msg['To'] = '604637630@qq.com'


s = smtplib.SMTP('smtp.qiye.163.com')
s.login('chengjianfeng@huiti.com', '1qaz2wsxP')
s.send_message(msg)
s.quit()