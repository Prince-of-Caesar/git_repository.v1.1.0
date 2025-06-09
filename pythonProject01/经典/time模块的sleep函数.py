#题目：暂停一秒输出。

#程序分析：使用 time 模块的 sleep() 函数。

import time  #引用时间

myD = {1: 'a', 2: 'b'}
for key, value in dict.items(myD):
    print(key, value)
time.sleep(10)

#暂停3秒输出
print('a', 'b')
