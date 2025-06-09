# 输入一行字符，利用 while 或 for 语句,分别统计出其中英文字母、空格、数字和其它字符的个数。
import string
#初始化
s = input('请输入一个字符串:\n')
alpha = 0
space = 0
digit = 0
others = 0
for i in s:
    # 判断字符i是否是一个“字母字符”，包括中文、英文、日文、韩文等
    if i.isalpha():
        alpha += 1
    elif i.isspace():
        space += 1
    elif i.isdigit():
        digit += 1
    else:
        others += 1
print('char =%d, space = %d, digit = %d, others = %d' % (alpha, space, digit, others))
