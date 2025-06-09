# 设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：

#  1、定义装饰器
import time
# wraps这个装饰器用来保留被装饰函数的元数据（如函数名、文档字符串等）。
from functools import wraps

def print_execution_time(func):
# wrapper函数: 它接受任意数量的位置参数和关键字参数（通过 *args 和 **kwargs）
# 这样就可以对任何函数进行包装而不用担心参数不匹配的问题。
    def wrapper(*args, **kwargs):
        start_time = time.time()  #记录开始时间
        result = func(*args, **kwargs)  #执行被装饰的函数
        end_time = time.time()  #记录结束时间
        excution_time = end_time - start_time  #计算执行时间
        print(f"函数 {func.__name__} 执行耗时：{excution_time:.2f} 秒")
        return result  #返回函数执行结果
    return wrapper

#  2、使用装饰器
@print_execution_time
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total
result = example_function(100)

print(result)