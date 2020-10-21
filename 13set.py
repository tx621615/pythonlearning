# set集合--元素不重复
'''
set:不存在重复的元素
1.创建的两种方式---{}, set(value), 特别是空集set()
2.增加元素:set.add(x)
3.删除元素:set.remove(x)
4.判断元素是否在set内: x in set
5.常用函数：set.clear(), len(set)



'''
# 创建 {}或者set(value),特别的空集合必须要用set()---{}表示空字典
s = {1, 2, 3, 4, 5, 6, 'abc'}
s1 = set()
print(s, s1)

# 一个或者多个元素的集合
s2 = set(('apple',))
print(s2)
s2 = set('apple')  # 不建议这么写
print(s2)

s2 = set(('apple', 'banana'))
print(s2)

# 添加元素
s1.add(1)
print(s1)
s1.add(3)
print(s1)
s1.add(0)
print(s1)

# 删除元素
s1.remove(1)
print(s1)
s1.remove(0)
print(s1)

# 另一种方法（可以增加多个元素，每个元素可以为字典，元组，列表）
s1.update([0, 1], (1, 4, 5))
print(s1)

# 随机删除---少用
s1.pop()
print(s1)
s1.pop()
print(s1)

# 计算元素个数
print(len(s1))

# 清空集合
s1.clear()
print(s1)

# 判断元素是否在集合内---最重要
s1 = {1, 2, 3, 4, 5, 6}
print('1是否在集合内', 1 in s1)
print('19是否在集合内', 19 in s1)