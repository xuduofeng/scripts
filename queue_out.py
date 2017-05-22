__author__ = 'derek'
import stomp
import time

class MyListener(object):
    def on_error(self, headers, message):
        print('received an error %s' % message)
    def on_message(self, headers, message):
        print('received a message %s' % message)
        #time.sleep(1)

conn = stomp.Connection10([('192.168.11.106',61613),('192.168.11.105',61613),('192.168.1.187',61613),('192.168.11.106',61623),('192.168.11.105',61623),('192.168.1.187',61623)], reconnect_sleep_initial=10, reconnect_attempts_max=10)
conn.set_listener('', MyListener())
conn.start()
conn.connect()
for i in xrange(10000):
    conn.subscribe('message')
time.sleep(1) # secs
conn.disconnect()