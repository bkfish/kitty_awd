把`waf.php`放在合适的目录，在使用的地方`require_once('waf.php');`,log在`/tmp/logs/`目录下  
额额 后事
```
sudo find /var/www/ -type f -path "*.php" | xargs sed -i "s/<?php/<?php\nrequire_once('\/tmp\/waf.php');\n/g"
```
[小菜鸡被虐记录](https://kit4y.github.io/2019/06/17/First-AWD/)