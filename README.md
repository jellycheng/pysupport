# pysupport
```
封装python、算法、常用函数、类等代码库


```

## 使用
```
import sys
import os

pysupport_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/pysupport/src"
sys.path.append(pysupport_dir) # 设置查找目录

# 导入使用
from pysupport import time_util
print(time_util.get_current_time()) # 输出当前日期 2025-07-09 17:15:09


```
