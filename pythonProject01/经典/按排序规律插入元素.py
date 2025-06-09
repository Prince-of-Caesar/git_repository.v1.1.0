# 有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

'''
假设有一个升序数组：
arr = [1, 3, 5, 7, 9]
num = 6
插入后应得到：
[1, 3, 5, 6, 7, 9]
'''
'''
解题思路：
判断数组是升序还是降序
找到要插入的位置 index
使用 insert() 方法插入元素
'''

# arr: 一个已经排好序的数组（列表）,num: 要插入的数字
def insert_sorted(arr, num):
    #判断排序顺序：升序or降序：
    is_ascending = arr[-1] > arr[0]

    #找到插入位置：
    index = 0
    if is_ascending: #升序
        while index < len(arr) and arr[index] < num:
            index += 1
    else: #降序
        while index < len(arr) and arr[index] > num:
            index += 1
    #使用 .insert() 方法，在找到的位置插入元素，并返回整个数组。：
    arr.insert(index,num)
    return arr

#测试
arr = [1, 3, 5, 11, 21]
print("原数组：", arr)
num = int(input("请输入一个数："))
result = insert_sorted(arr, num)
print("插入后的数组：", result)