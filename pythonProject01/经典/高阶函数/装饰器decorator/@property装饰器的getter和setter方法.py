# 利用@property给一个Screen对象加上width和height属性，
# 定义一个只读属性 resolution 来计算并返回屏幕的分辨率（即宽度乘以高度）：

class Screen(object):
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为Screen对象绑定width和height两个属性
    def __init__(self, width=None, height=None):
        self.__width = width
        self.__height = height

    # width和height属性分别有一个getter方法（用于获取值）和一个setter方法（用于设置值）
    @property
    def width(self):
        """获取宽度"""
        return self.__width

    @width.setter
    def width(self,value):
        """设置宽度"""
        if not isinstance(value,(int,float)):
            raise ValueError('width must be a number')
        if value < 0:
            raise ValueError('width cannot be negative')
        self.__width = value

    @property
    def height(self):
        """获取高度"""
        return self.__height

    @height.setter
    def height(self, value):
        """设置高度"""
        if not isinstance(value, (int, float)):
            raise ValueError('width must be a number')
        if value < 0:
            raise ValueError('width cannot be negative')
        self.__height = value

    @property
    def resolution(self):
        """只读属性，获取分辨率"""
        if self.__width == None or self.__height == None:
            raise ValueError('width or height must be set before accessing resolution.')
        return self.__width * self.__height

# 通过 if __name__ == "__main__": 是 Python 中的一种惯用法，用来判断一个文件是被直接运行还是被导入到其他 Python 脚本中使用。
# 可以让某些代码仅在模块被直接运行时执行，忽略缩进引起的模块异常导入
if __name__=="__main__":
#示例
    screen = Screen()
    screen.width = 1920
    screen.height = 1080

    print("Width:",screen.width)
    print("Height:",screen.height)
    print("Resolution:",screen.resolution)


