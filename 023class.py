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
5.总结：
（1） 区分对象属性和类属性，类属性会复制到所有对象中，在对象中的只是一个副本，区别类函数和对象函数，可以在class定义外单独为一个对象绑定对象函数。
（2）定义类变量--直接，添加。 定义对象变量：1.__init__---self 2.函数中self.--不过要调用函数才会生效。 3.外部直接.添加
（3）__变量/函数名，私有--实际只是重命名了，伪private
"""

from types import MethodType

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

print("----------------------")
"""1. 使用对象创建的属性 称之为对象属性 只有当前对象里才存在
   2. 如果使用对象属性创建了一个和类里面同名的属性 那么调用的时候会优先查找对象里面的属性
   3. 使用类里面的方法的参数 self 创建的属性 也为对象属性
   4. 当使用对象.属性名来改类属性的时候 其实是在对象里面创建了一个同名的属性,类属性只是将其值复制给了各个对象，对象中类属性的改变只是改变了同名副本而已，并未改变类属性的实际值---区别于java中static变量。
   5. 当将对象里面同名的属性删除掉以后 还是可以调用类的属性（对象里只是副本）
   6. 不能再对象里 删除 类里面的属性 只有使用的权利
   7. 使用类操作过的属性 所有对象在调用类属性的时候 都是修改后的属性
"""

# 创建类属性：在类中非方法块中的属性
# 创建实例属性

# class块中定义的方法都是类方法所有对象均可以使用
class A:
    # 类属性----创建类属性--------方法1
    i = 1234

    # 通过构造函数创建对象属性--方法一
    def __init__(self, name, age, w):
        self.name = name
        self.age = age
        self.__weight = w  # 私有属性--实际可以直接访问只是名字进行了修改

    # 通过方法创建的对象属性--使用第3点--方法二

    def createVar(self):
        self.xx = 'oo'


a = A('tx', 24, 80)
a.sno = "1234567"  # 创建对象属性--方法三
A.j = 4567  # 创建类属性---方法2
print(a.j)
print(A.j)
print(a.sno)
a.createVar()  # 在非构造方法中创建的属性，必须先运行才会创建，才可以使用，而在构造方法中创建的属性调用构造方法时就已经创建了，可以使用了。
print(a.xx)

print("-------------------------")
# 验证对象属性只是类属性的副本
print(a.i)
print(A.i)
a.i = 1
print(a.i)
print(A.i)


print("=========================")
# 给实例和对象绑定方法


def func(self, name):
    print("object's function: ", name)


a1 = A('tx', 24, 80)

# 绑定方法，特意为该对象绑定方法
a1.func = MethodType(func, a1)
a1.func('a1')
# a.func("a") --该对象没有该函数
# 外部添加绑定类的方法


def classfunc(self, name):
    print("class function: ", name)

A.classfunc = classfunc
a.classfunc("a")
a1.classfunc("a1")

