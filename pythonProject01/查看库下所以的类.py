#  dir() 是一个内置函数，它可以返回任何对象（包括模块、类、实例等）的属性和方法的列表。
#  如果你想要查看某个库或模块中的所有内容，你可以简单地传入该模块的对象
# import xlwt
# print(dir(xlwt))



#  这段代码会过滤出属于 xlwt 模块的类，并打印出来
import string
import inspect

# 打印 xlwt 模块中所有的类
for name, Tkinter in inspect.getmembers(string):
    if inspect.isclass(Tkinter):
        print(name)