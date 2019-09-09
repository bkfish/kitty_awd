#!/usr/bin/env python
#-*-coding:utf-8-*-
import re
import paramiko
import socket
import pandas as pd

ippath="ip.txt"
username='XXX'
oldpasswd = 'XXX' ##旧密码
newpasswd = 'XXX' ##新密码

#先从文本中匹配出ip
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

def demo(Ip,user,old_password,new_password):
    # 建立一个sshclient对象
    ssh = paramiko.SSHClient()
    # 允许将信任的主机自动加入到host_allow 列表，此方法必须放在connect方法的前面
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 调用connect方法连接服务器
    #如果远程执行命令错误信息是b'the input device is not a TTY\n' 去掉docker exec -it 中的t就好了
    try:
        ssh.connect(hostname=Ip, port=22, username=user, password=old_password,timeout=1)
        command = "passwd %s" %(user)
        stdin, stdout, stderr = ssh.exec_command(command.encode("utf-8"))
        #\n模拟回车 输两次密码
        stdin.write((new_password + '\n' + new_password + '\n').encode("utf-8"))
        out, err = stdout.read().decode("utf-8"), stderr.read().decode("utf-8")
        successful = 'password updated successfully'
        total_out=str(err)+str(out)
        if successful in total_out or "成功" in total_out:
            print(Ip + " 密码修改成功！密码为："+new_password)
            with open(newpasswd+'.txt','a') as f:
            	f.write(Ip + '\n')
        else:
            print('\t错误：\t' + str(err))
            print(Ip + " 密码修改失败！")
        # 关闭连接
        ssh.close()
    except paramiko.ssh_exception.AuthenticationException as e:
        print(Ip + ' ' + '\t账号密码错误!\t')
        with open('passerror.txt','a') as f:
            f.write(Ip + '\n')
    except socket.timeout as e:
        print(Ip + ' ' + '\t连接超时！\t')
        with open('timeoutssh.txt','a') as f:
            f.write(Ip + '\n')

if __name__ == "__main__":
    for ip in iplist:
        demo(ip,username,oldpasswd,newpasswd)
        #demo(ip,"root",newpasswd,oldpasswd)