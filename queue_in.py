__author__ = 'derek'
import stomp


#conn = stomp.Connection10([('192.168.11.106',61613),('192.168.11.105',61613),('192.168.1.187',61613),('192.168.11.106',61623),('192.168.11.105',61623),('192.168.1.187',61623)])
conn = stomp.Connection10([('activemq.huiti.com',61613)])
conn.start()
conn.connect()
for i in xrange(10):
    conn.send('message ', 'message ' + str(i), headers={'persistent': 'true'})
print("send ok")
conn.disconnect()