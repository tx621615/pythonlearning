'''
    六大内置类型
    1.Number -- int float bool complex
    2.String
    3.list
    4.tuple
    5.dictionary
    6.set
    其中最常用的为list and tuple
    不可变类型--number, string, tuple
'''

'''
list主要操作：
增 末尾增，任意索引位置增加
删
改
查 按值查找
创建 创建空表， []
拼接 只能list之间相互拼接
元素访问 按下标访问

list常用函数:
list(tuple/string)
list.append(obj)
list.insert(index, obj)
del
list.index(obj)

'''

# list的创建，方括号加逗号，类型可以不一致，可以一致
l = ['a', 'b', 1, 2]
list1 = ['red', 'green', 'blue', 'yellow', 'white', 'black']

# list创建另一种方式,使用元组或者字符串初始化，主要掌握空的初始
l1 = []
print(l1)
print(list())

# list访问--下标
print(l[0])
print(l[-1])

# 截取list元素---子连续list
print(l[0:3])

# 更新元素
print('list[0] = ' + l[0])
l[0] = 'd'
print('list[0] = ' + l[0])

# list末尾添加元素append()，任意位置插入元素--insert(index, obj)
l.append(3)
print(l)
list1.insert(1, 'redcopy')
print(list1)

# 删除元素del
print('原始列表: ', l)  # 字符串只能和字符串拼接，List不会自动调用toString方法
del l[2]
print('删除元素后的列表: ', l)

# 查找 list.index(obj) 返回第一个匹配项的索引--按值查找
print(l)
print('2 在list中的位置: ', l.index(2))

# 列表的拼接--可以用作增加元素
squares = [1, 4, 9, 16, 25]
squares += [36, 49, 64, 81, 100]
print(squares)
