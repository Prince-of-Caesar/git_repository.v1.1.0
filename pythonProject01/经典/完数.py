# 一个数如果恰好等于它的因子之和，这个数就称为"完数"。
# 例如6=1＋2＋3.编程找出1000以内的所有完数。
def is_perfect_number(n):
    factors = [i for i in range(1, n) if n % i == 0]
    return sum(factors) == n, factors
print("1000以内的完数和因子有：")

for num in range(1, 1001):
    perfect, factors = is_perfect_number(num)
    if perfect:
        print(f"{num}是完数,因子为：{factors}")


