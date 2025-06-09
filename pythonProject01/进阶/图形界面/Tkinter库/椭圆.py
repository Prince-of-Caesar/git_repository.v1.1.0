if __name__ == '__main__':
    from tkinter import *
    x = 360
    y = 160
    top = y - 30
    bottom = y - 30

    canvas = Canvas(width = 500, height = 600, bg = 'white')
    for i in range(20):
        canvas.create_oval(250 - top, 300 - bottom, 250 + top, 300 + bottom)
        top -= 5  #上边距变小（椭圆向上压缩）
        bottom += 5  #下边距变大（椭圆向下拉伸）
        #这就导致椭圆形状逐渐从一个正圆变成扁长的椭圆，然后又变成反方向拉长的椭圆，形成类似心跳或呼吸的效果
    '''
    视觉效果说明：
循环次数	top 值	bottom 值	椭圆形状
第1次	130	130	正圆
第2次	125	135	向上压缩、向下拉伸
第3次	120	140	更加拉伸
...	...	...	...
第10次	85	175	高度拉伸的椭圆
第11次	80	180	开始反向拉伸
...	...	...	...
    '''
canvas.pack()
mainloop()