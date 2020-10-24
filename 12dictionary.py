# 字典 键值对，键的元素不可更改，键的值唯一

'''
dict:
    1.创建{},key唯一，且key不可变,---key只能为number,string,tuple
    2.访问 dict[key]
    3.修改 dict[key] =
    4.增加 dict[newkey] = newvalue
    5.查: key in dict
    6.长度: len(dict)---key数
    7.删除: del dict[key] , 清空： dict.clear()



'''

# 创建
d1 = {'abc': 456, 98.6: 2}

# 访问--查
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

# 单引号和双引号都可以
print("dict['Name']: ", dict['Name'])
print("dict['Name']: ", dict["Name"])

# 修改
print("修改前 dic['Age']: ", dict['Age'])
dict['Age'] = 8
print("修改后 dic['Age']: ", dict['Age'])

# 增加元素--末尾添加
print("增加前：", dict)
dict['School'] = '菜鸟教程'
print("增加后：", dict)

# 删除元素del
print("删除前：", dict)
del dict['Name']
print("删除后：", dict)

# 清空字典
dict.clear()
print(dict)
del dict
print(dict['Name'])

# 常用函数 len(dict), key in dict
print('d1长度：', len(d1))
if 'abc' in d1:
    print('该键存在')