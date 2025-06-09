from operator import *

def calculator(a,b,k):
    return{
        '+':add,
        '-':sub,
        '*':mul,
        '/':truediv,
        '**':pow
# 通过键 k 从字典中获取对应的运算符函数。然后，使用该运算符对 a 和 b 进行计算。
    }[k](a,b)

print(calculator(1,4,'*'))
print(calculator(2,8,'-'))


# 链式操作：
def add_or_sub(a,b,oper):
    return(add if oper=='+'else sub)(a,b)

print(add_or_sub(69,12,'-'))