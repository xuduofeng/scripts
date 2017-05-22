#-*- encoding:utf-8 -*-
__author__ = 'derek'
#-*- encoding:utf-8 -*-
import jenkins
import time
jenkins_server_url='http://jenkins.test.smartcourt.cn'


user_id='chengjianfeng'
api_token='9bee7df1a7e814bf9c40ea6396219d52'


server = jenkins.Jenkins(jenkins_server_url, username=user_id, password=api_token)


#server.assert_job_exists()


# for view in server.get_views():
#     for job in server.get_jobs(view_name=view['name']):
#             print(job['name'])


#print(server.get_job_info('gpgame3.2.4-api-gp-games'))
print(server.get_view_config('v3.0-gpgame'))
#deploy_jobs = server.get_jobs(view_name = 'All')
#print('deploy_jobs ', deploy_jobs)


job_name = 'el-gamev4.1-order'
#获取job名为job_name的job的下次构建号
#next_bn = server.get_job_info(job_name)['nextBuildNumber']


#构建job，附加参数信息
#server.build_job(job_name,parameters={'env':'dev1', 'deploy':'no'})
#time.sleep(10)

#查询正在构建的队列
#print(server.get_queue_info())

#判断job名为job_name的job的某次构建是否还在构建中
#while server.get_build_info(job_name, next_bn)['building']:
#    print('status: ', server.get_build_info(job_name, next_bn)['building'])
#    time.sleep(2)



# print(server.get_job_info('video-APP-app-apis')['lastBuild']['number'])


#print(server.get_build_console_output('el-gamev4.1-order', next_bn))

# print(server.get_job_info('video-APP-app-apis')['builds'][0]['number'])
# print(server.get_build_info('video-APP-app-apis', 17))


#获取job名为job_name的job的某次构建的执行结果状态
#print(server.get_build_info('el-gamev4.1-order',next_bn)['result'])






