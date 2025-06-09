# Python支持多种图形界面的第三方库，包括：Tk，wxWidgets，Qt，GTK
# 但是Python自带的库是支持Tk的Tkinter，使用Tkinter，Tkinter封装了访问Tk的接口，
# Tk是一个图形库，支持多个操作系统，使用Tcl语言开发；
# Tk会调用操作系统提供的本地GUI接口，完成最终的GUI。无需安装任何包，就可以直接使用进行GUI编程

# 来编写一个GUI版本的“Hello, world!”
from tkinter import *
# 从Frame派生一个Application类，这是所有Widget的父容器：
# widget是指可以放置于屏幕上的图形元素或控件，比如按钮、滚动条、文本框等。它们是构成用户界面的基本组成部分，允许用户与程序进行交互。
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        # self.pack()是简单的布局，grid()可以实现更复杂的布局。
        # self.pack()负责将控件（widget）自动放置在父容器中，开始布局并根据一定的规则进行排列.
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.hellonLabel = Label(self, text = 'Hello, world!')
        self.hellonLabel.pack()
        # 当Button被点击时，触发self.quit()使程序退出。
        self.quitButton = Button(self, text = 'Quit', command = self.quit)
        self.quitButton.pack()
    # 在GUI中，每个Button、Label、输入框等，都是一个Widget。Frame则是可以容纳其他Widget的Widget，所有的Widget组合起来就是一棵树。

# 实例化Application，并启动消息循环：
app = Application()
#设置窗口标题
app.master.title('Hello, world!')
#主消息循环
app.mainloop()

