# 回数是指从左向右读和从右向左读都是一样的数，
# 例如12321，909。请利用filter()筛选出回数：

def is_palindrome(n):
    # 将数字转换成字符串
    str_n = str(n)
    #比较字符串与反转后结果是否相同
    return str_n == str_n[::-1]

print(list(filter(is_palindrome, range(1, 100))))

