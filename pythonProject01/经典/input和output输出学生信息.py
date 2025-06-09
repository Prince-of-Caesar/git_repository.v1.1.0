# 编写input()和output()函数输入，输出5个学生的数据记录。


'''
input_student()：用于输入一个学生的数据记录
output_student()：用于输出一个学生的数据记录
我们假设每个学生的信息包括：

学号（student_id）
姓名（name）
年龄（age）
成绩（score）
'''

def input_student():
    """
    输入一个学生信息，返回学生信息的字典
    """
    student= {}
    student['student_id'] = input("请输入学号：")
    student['name'] = input("请输入姓名：")
    student['age'] = int(input("请输入年龄："))
    student['score'] = float(input("请输入成绩："))
    return student

def output_student(student):
    """
    输出一个学生的信息
    """
    print("\n学生信息如下：")
    print(f"学号：{student['student_id']}")
    print(f"姓名：{student['name']}")
    print(f"年龄：{student['age']}")
    print(f"成绩：{student['score']}")
    print("-" * 30)  #打印一个由 30 个短横线（-）组成的分隔线

#主程序部分：
student = []
for i in range(1):
    print(f"\n请输入第{i + 1}个学生的信息：")
    stu = input_student()
    student.append(stu)

print("\n输出所有学生的信息：")
for stu in student:
    output_student(stu)