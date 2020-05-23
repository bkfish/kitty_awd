import requests
import re
import time
judge_url="http://39.100.119.37:10000/commit/flag"
self_token="Hello_kitty"
flag_list=[]
f=open('flag.txt','r')
flag_data=f.read()
flag_list=re.findall(r'flag{[a-zA-Z1-9\-]*}', flag_data)
print(flag_list)        

def post_rep(flag, token):
    headers={'Content‐Type':'application/json'}
    data = {
        'token': token,
        'flag':flag
    }
    rep = requests.post(judge_url, data=data)
    print(rep.content)
    print("send flag success "+flag+rep.text)
    time.sleep(1)

for flag in flag_list:
    rel_flag=''.join(str(i) for i in flag)
    post_rep(rel_flag,self_token)
