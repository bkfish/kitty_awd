import requests
judge_url="http://192.168.1.114/1.php"
self_token="Hello_kitty"
flag_list=[]
with open('flag.txt','r') as f:
    for line in f:
        flag_list.append(list(line.strip('\n').split(',')))
#print(flag_list)        

def post_rep(flag, token):
    param = {
        'token': token,
        'flag':flag
    }
    rep = requests.post(judge_url, data=param)
    #print(rep)
    print("send flag success "+flag+rep.text)

for flag in flag_list:
    rel_flag=''.join(str(i) for i in flag)
    post_rep(rel_flag,self_token)
