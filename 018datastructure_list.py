# 数据结构
"""

list.append(x)
把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。
list.extend(L)
通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。
list.insert(i, x)
在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) 。
list.remove(x)
删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。
list.pop([i])
从列表的指定位置移除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被移除。（方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号，你会经常在 Python 库参考手册中遇到这样的标记。）
list.clear()
移除列表中的所有项，等于del a[:]。
list.index(x)
返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
list.count(x)
返回 x 在列表中出现的次数。
list.sort()
对列表中的元素进行排序。
list.reverse()
倒排列表中的元素。
list.copy()
返回列表的浅复制，等于a[:]。

"""

l = [66.25, 333, 333, 1, 1234.5]
print(l.count(333), l.count(66.25), l.count("x"))
print("插入前：", l)
# 任意索引位置处插入
l.insert(2, -1)
print(l)
# 末尾插入
l.append(333)
print(l)
# 删除第一个匹配元素
l.remove(333)
print(l)
# 逆转元素
l.reverse()
print(l)
# 排序
l.sort()
print(l)
# 查找
print("第一个匹配333的索引: ", l.index(333))


# 将列表当成堆栈用
l1 = [3, 4]
# 末尾添加元素
l1.append(5)
l1.append(6)
print(l1)

# 弹出元素
print("第一个弹出元素", l1.pop())   # 可以弹出任意位置的元素，不带参弹出末尾元素
print(l1)
print("第一个弹出元素", l1.pop())   # 可以弹出任意位置的元素，不带参弹出末尾元素
print(l1)

# 列表推导式
"""
1.通常如果每个序列元素存在一些推导共性，就可以用某个表达式表达
2.每个列表推导式都在 for 之后跟一个表达式，然后有零到多个 for 或 if 子句。
返回结果是一个根据表达从其后的 for 和 if 上下文环境中生成出来的列表。如果希望表达式推导出一个元组，就必须使用括号。 
"""


