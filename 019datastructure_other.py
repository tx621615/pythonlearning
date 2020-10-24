# set and dictionary
"""
1.集合是一个无序不重复元素的集。基本功能包括检测元素是否存在集合内和消除重复元素。
2.可以用大括号({})创建集合。注意：如果要创建一个空集合，你必须用 set() 而不是 {} ；后者创建一个空的字典，下一节我们会介绍这个数据结构。
3.两个集合的并，差，交，异或
"""

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # 删除重复的

print('orange' in basket)                 # 检测是否成员

print('crabgrass' in basket)


# 以下演示了两个集合的操作

a = set('abracadabra')
b = set('alacazam')
print(a)     # a 中唯一的字母
print(b)
# 注意用的是位的&，|---不是逻辑与and，or
# 差：在 a 中的字母，但不在 b 中
print(a - b)
# 并：在 a 或 b 中的字母
print(a | b)
# 交：在 a 和 b 中都有的字母
print(a & b)
# 异或：在 a 或 b 中的字母，但不同时在 a 和 b 中
print(a ^ b)


print("--------------dictionary---------------")
# dictionary
# dict构造--元组列表
dict1 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(dict1)
# dict构造--关键字参数---这是实参
dict2 = dict(sape=4139, guido=4127, jack=4098)
print(dict2)

# dictionary遍历--遍历key,遍历value,遍历key--value
d = {'张三': 100, "李四": 99, "王五": 88}
print(d)
# for循环默认是遍历dictionary的key的
for x in d:
    print(x)

# keys()--获取key值列表
print(d.keys())   # 返回key值列表
for x in d.keys():
    print(x)

# value()---获取value值列表
print(d.values())
for v in d.values():
    print(v)

# 获取key--value两种方法
# 第一种方式，通过key获取value
for k in d:
    print(k, d[k])

# 第二种方式 item()--获取键值元组列表
print(d.items())
for k, v in d.items():
    print(k, v)

