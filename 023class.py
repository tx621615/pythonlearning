# class使用
"""
1.类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
2.实例变量：在类的声明中，属性是用变量来表示的，这种变量就称为实例变量，实例变量就是一个用 self 修饰的变量。
3.对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
4.语法格式：
    class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
"""

# 一个简单的类


class Myclass:
    """一个简答的类实例"""
    i = 12345

    def f(self):
        return "hello world!"


x = Myclass()

print("Myclass的类属性i为: ", x.i)
print("Myclass类的方法f输出为: ", x.f())

# 构造方法__init__(),可以有参数也可以没有参数,注意构造函数不用和Class重名,没有定义的话会自动配置默认构造函数


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print(x.r, x.i)

# self代表类的实例，通过实例.传递给self


class Test:
    def ptr(self):
        print(self)  # <__main__.Test object at 0x00000264834B3A60>
        print(self.__class__)   # <class '__main__.Test'>


t = Test()
t.ptr()





