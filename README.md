把`waf.php`放在合适的目录，在使用的地方`require_once('waf.php');`,log在`/tmp/logs/`目录下  
额额 后事
```
sudo find /var/www/ -type f -path "*.php" | xargs sed -i "s/<?php/<?php\nrequire_once('\/tmp\/waf.php');\n/g"
```
[小菜鸡被虐记录](https://kit4y.github.io/2019/06/17/First-AWD/)
[中国技能大赛](https://kit4y.github.io/2019/09/10/2019%E4%B8%AD%E5%9B%BD%E6%8A%80%E8%83%BD%E5%A4%A7%E8%B5%9Bawd%E7%9A%84%E4%B8%80%E4%BA%9B%E6%80%9D%E8%80%83/)