if __name__ == '__main__':
    from tkinter import *

    #创建主窗口:
    root = Tk()
    #创建画布：
    canvas = Canvas(root, width = 300, height = 300, bg = 'green')
    canvas.pack(expand = YES, fill = BOTH)

    #第一组线向左上角扩散绘制：
    x0 = 263
    y0 = 263
    x1 = 275
    y1 = 275
    for i in range(19):
        canvas.create_line(x0, y0, x1, y1, width = 1, fill = 'red')
        x0 -= 5
        y0 -= 5
        x1 += 5
        y1 += 5

    #第二组线向右下角扩散绘制：
    x0 = 263
    y0 = 263
    y1 = 275
    for i in range(21):
        canvas.create_line(x0, y0, x0, y1, fill = 'red')
        x0 -= 5
        y0 -= 5
        y1 += 5

    # 启动主事件循环:
    mainloop()

