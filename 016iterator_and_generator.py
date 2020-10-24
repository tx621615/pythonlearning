# 迭代器和生成器

# 迭代器，string,list,tuple,dictionary,set均有迭代器,迭代器的两个方法iter(obj),next(iterator)
# 在for循环中，Python将自动调用工厂函数iter()获得迭代器，自动调用next()获取元素，还完成了检查StopIteration异常的工作。
# 使用for in语句只要序列对象实现了迭代器，那么都可以遍历
l = range(5)
it = iter(l)
try:
    while True:
        val = next(it)
        print(val)
except StopIteration:
    pass

# 把一个类作为一个迭代器使用只需要在类中实现两个方法 __iter__() 与 __next__() 。
# StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。

class  MyNumbers:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)  # 对于迭代器对象，for in语句自动调用其迭代器方法和next()方法然后赋值给x，因此可以直接在in后面写迭代器对象,因为iter（classobj）也是返回该class对象，所以不用多此一举
for x in myclass:
    print(x)

# 生成器
'''
1.生成器函数：
常规函数定义，但是，使用yield语句而不是return语句返回结果。yield语句一次返回一个结果，在每个结果中间，挂起函数的状态，以便下次重它离开的地方继续执行

2.生成器表达式：
类似于列表推导，但是，生成器返回按需产生结果的一个对象，而不是一次构建一个结果列表

3.生成器分为两部分，生成器的函数和生成器的迭代器，生成器的函数是用def定义，包含yield部分，调用该函数时返回一个生成器的迭代器对象，但代码不执行，每次请求一个值（使用next（）函数---隐式或者显示，才会执行函数代码，执行到yield代码，就停止执行--挂起，等待下一次的执行，
一直到出错或者说return）
'''

# 最简单的生成器函数
def mySquare():
    i = 0
    while i < 5:
        yield i*i
        i += 1

for x in mySquare():
    print(x)

# 生成函数表达式与列表解析式区别一个用[]一个用(),生成函数表达式不会直接生成值而是调用的时候不断产生值，在大数据的时候非常有用

'''
列表解析(List comprehensions)
列表解析式是将一个可迭代对象（如列表）转换成另一个列表的工具。在转换过程中，可以指定元素必须符合某一条件，并按照指定的表达式进行转换，才能添加至新的列表中。
语法：
[expression for iter_var in iterable1] 

[expression for iter_var2 in iterable2 ...
                   for iter_varN in iterableN]

[expression for iter_var in iterable1
                    if condition]

生成器表达式（Generator expressions）
不创建列表，只是返回一个生成器。这个生成器在每次计算出一个条目后，才把这个条目产生出来。所以在处理大量数据时更有优势。
语法：
(expression for iter_var in iterable1)

(expression for iter_var2 in iterable2 ...
                   for iter_varN in iterableN)

(expression for iter_var in iterable1
                    if condition)
'''

l = [x for x in range(10)]
print(l)

g = (x for x in range(10))
print(g)  # <generator object <genexpr> at 0x0000022E52ADB890>

for x in g:
    print(x)

# 同样是遍历所有对象，generator只是一次返回一个值，但并不保存，但是列表是一次性生成所有值，同时进行了保存。在处理大数据的时候generator有很大的作用。
