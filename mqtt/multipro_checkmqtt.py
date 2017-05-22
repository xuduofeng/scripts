#!/usr/bin/env python
#coding:utf-8
#Author Aladin
import multiprocessing
import time
import os
import sys
import commands

#发送的所有字节数
def get_mqtt_broker_sent(interval):
    cmds = "/usr/bin/mosquitto_sub -t '$SYS/broker/bytes/sent' >> br_sent.txt"
    print "br_sent"
    commands.getstatusoutput(cmds)

#$SYS/broker/bytes/received  收到的所有字节数
def get_mqtt_broker_received(interval):
    cmds = "/usr/bin/mosquitto_sub -t '$SYS/broker/bytes/received' >> br_received.txt"
    print "br_received"
    commands.getstatusoutput(cmds)

#$SYS/broker/subscriptions/count
def get_mqtt_broker_subscriptions(interval):
    cmds = "/usr/bin/mosquitto_sub -t '$SYS/broker/subscriptions/count' >> subscriptions.txt"
    print "subscriptions"
    commands.getstatusoutput(cmds)


#===========clients==================================
#$SYS/broker/clients/connected 当前在线的客户端数
def get_mqtt_broker_connected(interval):
    cmds = "/usr/bin/mosquitto_sub -t '$SYS/broker/clients/connected' >> br_connected.txt"
    print "br_connected"
    commands.getstatusoutput(cmds)

##$SYS/broker/clients/expired  超时的连接数
def get_mqtt_broker_expired(interval):
    cmds = "/usr/bin/mosquitto_sub -t '$SYS/broker/clients/expired' >> br_expired.txt"
    print "br_expired"
    commands.getstatusoutput(cmds)
#$SYS/broker/clients/disconnected 断开的连接数
def get_mqtt_broker_disconnected(interval):
    cmds = "/usr/bin/mosquitto_sub -t '$SYS/broker/clients/disconnected' >> br_disconnected.txt"
    print "br_disconnected"
    commands.getstatusoutput(cmds)

#$SYS/broker/clients/maximum  最大并发连接数
def get_mqtt_broker_maximum(interval):
    cmds = "/usr/bin/mosquitto_sub -t '$SYS/broker/clients/maximum' >> br_maximum.txt"
    print "br_maximum"
    commands.getstatusoutput(cmds)

#$SYS/broker/clients/total  所有连接数（活动的和非活动的）
def get_mqtt_broker_total(interval):
    cmds = "/usr/bin/mosquitto_sub -t '$SYS/broker/clients/total' >> br_total.txt"
    print "br_total"
    commands.getstatusoutput(cmds)


################### Load  ====================================
##$SYS/broker/publish/messages/sent
def get_mqtt_p_sent(interval):
    cmds = "/usr/bin/mosquitto_sub -t '$SYS/broker/publish/messages/sent' >> p_sent.txt"
    print "p_sent"
    commands.getstatusoutput(cmds)

#$SYS/broker/publish/messages/received
def get_mqtt_p_received(interval):
    cmds = "/usr/bin/mosquitto_sub -t '$SYS/broker/publish/messages/received' >> p_received.txt"
    print "p_received"
    commands.getstatusoutput(cmds)

#====-----Messages = =============================================
#$SYS/broker/messages/sent
def get_mqtt_m_sent(interval):
    cmds = "/usr/bin/mosquitto_sub -t '$SYS/broker/messages/sent' >> m_sent.txt"
    print "m_sent"
    commands.getstatusoutput(cmds)
#$SYS/broker/messages/stored
def get_mqtt_m_stored(interval):
    cmds = "/usr/bin/mosquitto_sub -t '$SYS/broker/messages/stored' >> m_stored.txt"
    print "m_stored"
    commands.getstatusoutput(cmds)
#$SYS/broker/messages/received
def get_mqtt_m_received(interval):
    cmds = "/usr/bin/mosquitto_sub -t '$SYS/broker/messages/received' >> m_received.txt"
    print "m_received"
    commands.getstatusoutput(cmds)
#$SYS/broker/messages/inflight 发送中的消息
def get_mqtt_m_inflight(interval):
    cmds = "/usr/bin/mosquitto_sub -t '$SYS/broker/messages/received' >> m_inflight.txt"
    print "m_inflight"
    commands.getstatusoutput(cmds)

if __name__ == "__main__":
    p1 = multiprocessing.Process(target = get_mqtt_broker_sent, args = (2,))
    p2 = multiprocessing.Process(target = get_mqtt_broker_received, args = (3,))
    p3 = multiprocessing.Process(target = get_mqtt_broker_subscriptions, args = (4,))
    p4 = multiprocessing.Process(target = get_mqtt_broker_connected, args = (5,))
    p5 = multiprocessing.Process(target = get_mqtt_broker_expired, args = (6,))
    p6 = multiprocessing.Process(target = get_mqtt_broker_disconnected, args = (7,))
    p7 = multiprocessing.Process(target = get_mqtt_broker_maximum, args = (8,))
    p8 = multiprocessing.Process(target = get_mqtt_p_sent, args = (9,))
    p9 = multiprocessing.Process(target = get_mqtt_p_received, args = (10,))
    p10 = multiprocessing.Process(target = get_mqtt_m_sent, args = (11,))
    p11 = multiprocessing.Process(target = get_mqtt_m_stored, args = (12,))
    p12 = multiprocessing.Process(target = get_mqtt_m_received, args = (13,))
    p13 = multiprocessing.Process(target = get_mqtt_m_inflight, args = (14,))
    p14 = multiprocessing.Process(target = get_mqtt_broker_total, args = (15,))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p9.start()
    p10.start()
    p11.start()
    p12.start()
    p13.start()
    p14.start()