# 继承
"""
1.单继承：class DerivedClassName(BaseClassName1):
2.多继承:class DerivedClassName(Base1, Base2, Base3):
需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法。

"""


class People:
    name = ""
    age = 0
    __weight = 0

    def __init__(self, n, a, w):  # 常见错误init 写成了int
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我%d岁。"%(self.name, self.age))


# 单继承示例
class Student(People):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构造方法
        People.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法

    def speak(self):
        print("%s 说：我%d岁了，我在读%d几年级"%(self.name, self.age, self.grade))


# 另一个类多重继承之前的准备


class Speaker():
    topic = ""
    name = ""

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


class Sample(Speaker, Student):
    a = ""
    # 另一种调用父类构造函数的方法 note：多继承只能使用第一个父类的构造函数，因为第一个的构造函数必定匹配，同时super(ClassName, obj).这是通过对象调用所以self不用写，而通过类名调用，self变量必须加上

    def __init__(self, n, a, w, g, t):
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, t)


test = Sample("Tim", 25, 80, 4, "Python")
test.speak()  # 结果显示方法在子类中未找到时，从左到右查找父类中是否包含方法。

s1 = Student("Tim", 25, 80, 4)
s1.speak()

# 方法重写以及调用父类的方法


class Parent:  # 定义父类
    def myMethod(self):
        print('调用父类方法')


class Child(Parent):  # 定义子类
    def myMethod(self):
        print('调用子类方法')


# 动态绑定，即对象是什么就调用哪个对象的相关方法----python中没有多态
c = Child()  # 子类实例
c.myMethod()  # 子类调用重写方法
super(Child, c).myMethod()  # 用子类对象调用父类已被覆盖的方法
p = Parent()
p.myMethod()

"""
类的专有方法：
__init__ : 构造函数，在生成对象时调用
__del__ : 析构函数，释放对象时使用
__repr__ : 打印，转换
__setitem__ : 按照索引赋值
__getitem__: 按照索引获取值
__len__: 获得长度
__cmp__: 比较运算
__call__: 函数调用
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__truediv__: 除运算
__mod__: 求余运算
__pow__: 乘方
__str__：对象描述信息
"""

# 运算符重载---即对类的专有方法就行重载


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # 定义print返回内容(对象的描述信息) 定义前返回内存地址<__main__.Vector object at 0x0000017A768BA310>  定义后返回Vector(2, 10)
    def __str__(self):
        return 'Vector(%d, %d)'%(self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1)
print(v2)
print(v1 + v2)