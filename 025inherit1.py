# 类变量和成员变量的继承规则
"""
1，对于类变量x，最开始Children1和Children2都没有赋值x，所以都等于1。当Children1赋值2之后值就变了，但Children2还是之前的1，当父类修改为3后，由于Children2一直没有赋值，所以等于修改后的父类的x值3，直到Children2自己赋值才是4。
2，对于实例变量y，最开始child1和child2都没有对y赋值，所以都等于1。当child1变成2之后就变成2，但child2还是之前的1，即使父类实例par改变y的值为3，child2还是为1。直到child2自己赋值为4才改变。
1，对于类变量x，最开始Children和GrandChildren都没有赋值x，所以都等于1。当Children赋值2之后值就变了，GrandChildren也跟着变，当父类修改后，由于Children2在之前赋值为2，所以即使修改了父类的x，但也不会访问到他。GrandChildren自己赋值为3就会变成4，不影响Parent和GrandChildren。
2，对于实例变量y，最开始child和grand都没有对y赋值，所以都等于1。当child变成2之后就变成2，但grand还是最开始的初值1，即使父类实例par改变y的值为3，grand还是1。直到grand自己赋值为4才改变。

总结：对于类变量来说，当子类没有赋值类变量，那么就会随父类的类变量的值改变而改变，一旦子类自身赋值过后则与父类类变量没有关系了。
对于成员变量，除了最开始的继承值外，则无任何关系。
"""
class Parent(object):
    x = 1  # 类变量

    def __init__(self):
        self.y = 1  # 实例变量


class Children1(Parent):
    pass


class Children2(Parent):
    pass


par = Parent()  # 具体的类实例对象
child1 = Children1()  # 具体的类实例对象
child2 = Children2()  # 具体的类实例对象
print('-------------------------------------')
print('Parent.x=', Parent.x, ',Children1.x=', Children1.x, ',Children2.x=', Children2.x)
print('par.y=', par.y, ',child1.y=', child1.y, ',child2.y=', child2.y)

print('-------------------------------------')
Children1.x = 2
child1.y = 2
print('Parent.x=', Parent.x, ',Children1.x=', Children1.x, ',Children2.x=', Children2.x)
print('par.y=', par.y, ',child1.y=', child1.y, ',child2.y=', child2.y)

print('-------------------------------------')
Parent.x = 3
par.y = 3
print('Parent=', Parent.x, ',Children1=', Children1.x, ',Children2=', Children2.x)
print('par.y=', par.y, ',child1.y=', child1.y, ',child2.y=', child2.y)

print('-------------------------------------')
Children2.x = 4
child2.y = 4
print('Parent=', Parent.x, ',Children1=', Children1.x, ',Children2=', Children2.x)
print('par.y=', par.y, ',child1.y=', child1.y, ',child2.y=', child2.y)

