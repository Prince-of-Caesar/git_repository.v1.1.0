from turtle import *

def drawStar(x, y):
    #提起画笔，移动时不绘图
    pu()
    #将海龟移动到(x, y)位置
    goto(x, y)
    #放下画笔，开始绘图
    pd()
    #seth()代步海龟面向的角度(Set Heading)，设置海龟的方向为0度，即指向正方向
    seth(0)

    for i in range(5):
        #fd是forward的缩写，让海龟向后移动90像素
        fd(-90)
        #rt是right的缩写，向右转144度
        rt(144)

#绘制一系列五角星：
#沿着X轴每隔50像素绘制一个五角星，起始于x=0并结束于x=200，共绘制5个五角星(在x=0，50，100，150，200处)
for x in range(0, 450, 90):
    # 每个五角星都位于y=0的水平线上
    drawStar(x, 0)
