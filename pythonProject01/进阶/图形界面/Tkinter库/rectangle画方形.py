if __name__ == '__main__':
    from tkinter import *

    root = Tk()
    root.title('Canvas')
    '''
    geometry() 的作用
    功能      	示例	                        说明
    设置窗口大小	root.geometry("800x600")	宽度 800px，高度 600px
    设置窗口位置	root.geometry("+500+300")	距离左侧 500px，顶部 300px
    同时设置大小和位置	root.geometry("800x600+500+300")	最常用的形式
    '''
    root.geometry("800x600+500+300")
    canvas = Canvas(root, width = 800, height = 800, bg = 'yellow')

    x0 = 403
    y0 = 403
    x1 = 385
    y1 = 385

    for i in range(19):
        canvas.create_rectangle(x0, y0, x1, y1)
        x0 -= 8
        y0 -= 8
        x1 += 8
        y1 += 8

    canvas.pack()
    root.mainloop()