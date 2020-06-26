import requests
import time
def tjflag1(flag):

    url="http://39.100.119.37:8080/api/v1/challenges/attempt"
    #data={"challenge_id":2,"submission":""+flag+""}
    data='{"challenge_id":1,"submission":"'+flag+'"}'
    h = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
"Accept-Encoding": "gzip, deflate",
"CSRF-Token":"67a699cc8bf59dfd75a690fc82339eb2de9b4bb015141511feb200b4f0b23977",
"Connection": "keep-alive",
"Content-Type": "application/json"
}
    cookies={"session":"e2dcb7dd-2875-4805-bc15-ccdea34617c2","PHPSESSID":"jnr3quolg5o2ohlifbdld6bku5"}
    req=requests.post(url=url,data=data,cookies=cookies,headers=h)
    print(req.text)

def ftjflag1():
    with open("./sendflag.txt") as f:
        for a in f:
            print(a.strip())
            time.sleep(2)
            tjflag1(a.strip())
ftjflag1()