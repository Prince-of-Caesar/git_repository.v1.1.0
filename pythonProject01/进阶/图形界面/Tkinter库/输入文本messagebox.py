# messagebox 是 tkinter 模块中的一个子模块，用于创建和显示各种对话框窗口，如信息提示、警告、错误消息等。
# 使用 messagebox 可以方便地向用户展示信息或获取用户的确认反馈。

# 我们再对这个GUI程序改进一下，加入一个文本框，让用户可以输入文本，然后点按钮后，弹出消息对话框。
from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()

        self.alterButton = Button(self, text='Hello', command=self.hello)
        self.alterButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)

app = Application()
#设置窗口标题
app.master.title('王小明')
#主消息循环
app.mainloop()
