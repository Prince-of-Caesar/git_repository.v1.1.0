# 求输入数字的平方，如果平方运算后小于 50 则退出。

# 接收用户输入的数字，计算它的平方；如果平方结果小于 50，则退出循环:
while True:
    try:
        num = int(input("Enter a number: "))
        square = num * num

        if square < 50:
            print(f"{num}的平方是{square}, 小于50，程序退出。")
            break
        else:
            print(f"{num}的平方是{square}")
    except ValueError:
        print("输入无效，请输入一个整数。")