# asuri金科校赛awd准备
## Web 攻
 一、使用`segment_To_file.py`把所有ip写入`ip_file.txt`中(不定参数为C端，一般输入1，注意1.1结尾的为路由器可能需要删除)      

 二、`get_flag_to_file.py`使用`ip_file.txt`的ip文本数据批量获取flag放在`flag.txt`文件中(不定核心参数为getflag函数)     

 三、`send_flag.py`使用`flag.txt`批量提交(不定参数为裁判机url+自己的token) 




## Pwn 攻 
修改`get_flag_to_file`中的`getflag`函数  
 
## Web 防
 把`Flow_Analysis.php`放在根目录，在使用的地方`require_once('Flow_Analysis.php');`,log在`\logs\`目录下  