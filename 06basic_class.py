#06基本数据类型
#python中变量不用类型，即不用声明，使用前必须赋值
counter = 100   #整形
miles = 1000.0  #浮点型
name = "runoob" #字符串

print(counter)
print(miles)
print(name)

#多个变量赋值
a = b = c = 1
print(a)
a, b, c = 1 , 2, 'abc'
print(c)

#type的使用
#Number--int, float, complex, bool
a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d)) #<class 'int'> <class 'float'> <class 'bool'> <class 'complex'>

#数值运算
print(2 / 4) #除法产生一个浮点数 0.5
print(4 / 2)    #2.0
print(2 // 4)   #除法产生一个整数 0
print(4 // 2)   #2
print(2 ** 4) #乘方

#一个变量可以通过赋值指向不同类型对象