import math
from tkinter import *

class PTS:
    def __init__(self):
        self.x = 0
        self.y = 0
points = []

def LineToDemo():
    screenx = 400
    screeny = 400
    canvas = Canvas(width = screenx, height = screeny, bg = 'white')

    #设置一个比例因子，调整显示内容的宽高比:
    AspectRatio = 0.85
    #定义一个整数常量，表示要绘制的点,代表有多少个顶点。
    MAXPTS = 15
    h = screeny
    w = screenx
    xcenter = w / 2
    ycenter = h / 2
    radius = (h - 30) / (AspectRatio * 2) - 20
    step = 360 / MAXPTS
    angle = 0.0

    for i in  range(MAXPTS):
        rads = angle * math.pi / 180.0
        p = PTS()
        p.x = xcenter + int(math.cos(rads) * radius)
        p.y = ycenter - int(math.sin(rads) * radius * AspectRatio)
        angle += step
        points.append(p)
    canvas.create_oval(xcenter - radius, ycenter - radius, xcenter +radius, ycenter +radius)

    for i in range(MAXPTS):
        for j in range(MAXPTS):
            canvas.create_line(points[i].x, points[i].y, points[j].x, points[j].y )

    canvas.pack()
    mainloop()
if __name__ == '__main__':
    LineToDemo()