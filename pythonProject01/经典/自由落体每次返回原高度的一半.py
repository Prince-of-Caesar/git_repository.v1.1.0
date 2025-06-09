# 一球从100米高度自由落下，每次落地后反跳回原高度的一半,再落下;
# 求它在第10次落地时，共经过多少米？第10次反弹多高？

'''
第一次下落：100 米
第二次下落 + 上升：100/2（上升）+ 100/2（下落）
第三次下落 + 上升：(100/2)/2 = 100/(2²)（上升）+ 同样高度下落
...
除第一次外，每次弹起再落下都会走 两倍的高度
'''

#  总路程 = 100 + 2*(50 + 25 + 12.5 + ...) 共9次反弹
#即总路程 = 100 + 2 * (100/2 + 100/4 + ... + 100/2^9)
#这是一个等比数列前n项和的问题。

height = 100
total_distance = height  #第1次下落100米
bounce_height = height  #弹跳高度

for i in range(2,11):  #记录第2次到第10次
    # bounce_height = bounce_height / 2 等价于
    bounce_height /= 2
    total_distance += bounce_height * 2

print(f"第10次落地时共经过{total_distance:.4f} 米")
print(f"第10次反弹高度为{bounce_height:.4f} 米")
