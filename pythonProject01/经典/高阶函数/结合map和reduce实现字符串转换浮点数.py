# 实现一个 str2float 函数，将字符串 '123.456' 转换成浮点数 123.456，
# 并且要求使用 Python 的 map 和 reduce 函数。

#  1. 将字符串拆分为整数部分和小数部分：
#  2. 使用 map() 把每个字符转换成对应的数字：
#  3. 使用 reduce() 将这些数字组合成整数或小数：

#   小数0.456
#   x * 0.1 + y * 0.1,
#   ((0 * 0.1 + 4 * 0.1) * 0.1 + 5 * 0.1) * 0.1 + 6 * 0.1

#  先将 '456' 反转成 '654'反转字符串，再使用 reduce 累积
#  从最低位开始累积，每次乘以 0.1
#  执行过程：
#  初始值：x = 0
#  第一个数字：6 → (0 + 6) * 0.1 = 0.6
#  第二个数字：5 → (0.6 + 5) * 0.1 = 0.56
#  第三个数字：4 → (0.56 + 4) * 0.1 = 0.456


from functools import reduce
def str2float(s):
    #判断是否有小数点
    if '.' in s:
        int_part, frac_part = s.split('.')
    else:
        int_part, frac_part = s, ''
    #将字符串的每一位转为整数
    digits = list(map(int, int_part + frac_part))
    #计算整数部分的值
    int_value = reduce(lambda x,y: x * 10 + y, map(int, int_part), 0)
    #计算小数部分的值
    frac_part = reduce(lambda x,y: x * 0.1 + y * 0.1, map(int, frac_part[::-1]), 0)  #注意小数要反转

    #总值
    return int_value + frac_part
print(str2float('123.456'))  # 输出：123.456
print(str2float('789'))      # 输出：789.0
print(str2float('.123'))     # 输出：0.123
print(str2float('0.987'))    # 输出：0.987


