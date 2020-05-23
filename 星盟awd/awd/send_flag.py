import requests
def tjflag1(flag):

    url="http://39.100.119.37:8080/api/v1/challenges/attempt"
    #data={"challenge_id":2,"submission":""+flag+""}
    data='{"challenge_id":2,"submission":"'+flag+'"}'
    h = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
"Accept-Encoding": "gzip, deflate",
"CSRF-Token":"e9817606c5e5373499bd7e43b64c045b60a276b839b340c4f4a37c2eb27f4e8a",
"Connection": "keep-alive",
"Content-Type": "application/json"
}
    cookies={"session":"2deefa03-cda6-41fc-be25-a986067c7048","PHPSESSID":"jnr3quolg5o2ohlifbdld6bku5"}
    req=requests.post(url=url,data=data,cookies=cookies,headers=h)
    print(req.text)

def ftjflag1():
    with open("./web2.txt") as f:
        for a in f:
            print(a.strip())
            tjflag1(a.strip())
ftjflag1()