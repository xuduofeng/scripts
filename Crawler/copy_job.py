__author__ = 'derek'
#-*- encoding:utf-8 -*-
import jenkins
import time

user_id='chengjianfeng'

ori_view = 'user-rule-check'
dest_view = 'arena3.2'

items = ['module-garena-service','garenaJsp']

env = 'test'

if env == 'uat':
    #####uat######
    jenkins_server_url='http://jenkins.smartcourt.cn'
    api_token='76dcc2cbfbdcae067874de3ddf40ab85'
else:
    ######dev######
    jenkins_server_url='http://jenkins.test.smartcourt.cn'
    api_token='9bee7df1a7e814bf9c40ea6396219d52'

server = jenkins.Jenkins(jenkins_server_url, username=user_id, password=api_token)
'''
if server.view_exists(dest_view):
    print(dest_view + ' exists!!!')
else:
    server.create_view(dest_view, jenkins.EMPTY_VIEW_CONFIG_XML)

'''

for item in items:
    ori_job_name = ori_view + '-' + item
    dest_job_name =  dest_view + '-' + item

    print(not server.job_exists(dest_job_name))
    if (not server.job_exists(dest_job_name)):
        if server.job_exists(ori_job_name):
            server.copy_job(ori_job_name, dest_job_name)
        elif server.job_exists('gpgame3.2.4-' + item):
            ori_job_name = 'gpgame3.2.4-' + item
            server.copy_job(ori_job_name, dest_job_name)
        elif server.job_exists('weixin-' + item):
            ori_job_name = 'weixin-' + item
            server.copy_job(ori_job_name, dest_job_name)
        elif server.job_exists('POM-Build_' + item):
            ori_job_name = 'POM-Build_' + item
            server.copy_job(ori_job_name, dest_job_name)
        elif server.job_exists('trunk_new-' + item):
            ori_job_name = 'trunk_new-' + item
            server.copy_job(ori_job_name, dest_job_name)
        else:
            print(item + ' ori job can not find!!!')
            continue
        print (ori_job_name, dest_job_name)
    else:
        print(dest_job_name + ' already exists!!!')