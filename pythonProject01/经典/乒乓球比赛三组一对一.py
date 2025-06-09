# 两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。
# 已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。

'''
 解题思路：
我们让甲队的 a、b、c 分别与乙队的 x、y、z 的一个排列进行配对（即每个甲队队员对应一个不同的乙队队员）。
我们可以使用全排列的思想来遍历乙队的所有可能对手分配。
'''

#itertools提供了一系列函数用于创建迭代器（iterator）,可以高效地处理数据的排列、组合、笛卡尔积等操作。
import itertools
#甲队成员：
teamA = ['a', 'b', 'c']
#乙队成员：
teamB = ['x', 'y', 'z']

#permutations常用于枚举所有可能顺序的情况(不可重复)
#生成可迭代对象的所有排列,itertools.permutations() 是处理排列问题的强大工具。
#遍历乙队所有排序：
for perm in itertools.permutations(teamB):
    #将a,b,c分别与排列中的成员配对：
    opponentA = perm[0]
    opponentB = perm[1]
    opponentC = perm[2]

    #限制条件：
    if opponentA != 'x' and opponentC not in ['x', 'z']:
        print("找到符合条件的比赛名单：")
        print('甲队 对阵 乙队：')
        print(f"a vs {opponentA}")
        print(f"b vs {opponentB}")
        print(f"c vs {opponentC}")
        break  #找到后退出循环