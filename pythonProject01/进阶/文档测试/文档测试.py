#Python内置的doctest模块可以直接提取注释中的代码并执行测试

# 对函数fact(n)编写doctest：
def fact(n):
    """
    计算正整数 n 的阶乘（n!）

    >>> fact(0)
    1
    >>> fact(1)
    1
    >>> fact(5)
    120
    >>> fact(7)
    5040
    >>> fact(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be a non-negative integer.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# doctest.testmod()自动搜索调用它模块内的所有文档字符串。
# 如果所有示例都通过了，则不输出任何内容；如果有失败的情况，它会报告具体的错误信息。
if __name__ == "__main__":
    import doctest
    doctest.testmod()