# 杨辉三角定义如下：
#
#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1
# 理解杨辉三角的规律：每一行的第一个和最后一个元素都是1，中间的每个元素是上一行对应位置的两个相邻元素之和。
# 把每一行看做一个list，试写一个生成器generator，不断输出下一行的list：

def triangle():
    row = [1]  #初始化第一行
    while True:
        yield row  #输出当前行
        #计算下一行
        new_row = [1] #下一行的第一个元素总是1
        for i in range(len(row) - 1):
            new_row.append(row[i] + row[i + 1])  #中间元素是上一行相邻两数之和
        new_row.append(1)  #下一行的最后一个元素也是1
        row = new_row #更新当前行 为下一行

#测试生成器
genrator = triangle()
for _ in range(6):
    print(next(genrator))