# 输入输出
import math
"""
1.如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
2.如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
    (1)除了字符串类型外，使用str还是repr转换没有什么区别，字符串类型的话，外层会多一对引号，这一特性有时候在eval操作时特别有用；
    (2)命令行下直接输出对象调用的是对象的repr方法，print输出调用的是str方法
"""

# str.format()简单使用 note:print会简单去除最外层的引号
# 第一种简单{}
print('{}网址： "{}!"'.format("菜鸟教程", "www.runoob.com"))  # 传值的string引号会被去除

# 第二种位置参数，可以认为是参数元组对应索引的内容
print('{0}和{1}'.format('Google', 'Runoob'))
print('{1}和{0}'.format('Google', 'Runoob'))  # 实际调用的是tuple[i],i位对应的位置

# 第三种{variable name}  + 关键字参数
print('{name}的网址： "{url}"'.format(name='菜鸟教程', url='www.runoob.com'))

# str.format()混合使用
# 要点：{}不能和位置{i}混合使用，位置{i}与关键字混合使用时，关键字参数必须位于位置参数之后
print('站点列表{0}, {1} 和 {other}'.format('Google', 'Runoob', other='Taobao'))

# 可选项 : 和格式标识符可以跟着字段名
print('常量PI的值为: {0:.3f} '.format(math.pi))

# 传递对象或者列表元组字典之类可以使用 . / [] ,但必须使用位置参数或者关键字参数
infos = ['阿星', 9527]
food = ['霸王花', '爆米花']
print('我叫{0[0]}，警号{0[1]}，爱吃{1[0]}。'.format(infos, food)) # 我叫阿星，警号9527，爱吃霸王花。

table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))

# input
str = input("请输入: ")
print("你输入的内容是：", str)

