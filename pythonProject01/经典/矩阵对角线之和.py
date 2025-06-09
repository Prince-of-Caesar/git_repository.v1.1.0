# 求一个3*3矩阵主对角线元素之和。
def sum_diagonal(matrix):
    #any(len(row) != 3 for row in matrix):检查每一行的列数是否都是3。
    if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
        raise ValueError("Matrix must be 3x3 matrix")
    return matrix[0][0] + matrix[1][1] + matrix[2][2]

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print("主对角线元素之和为：", sum_diagonal(matrix))

