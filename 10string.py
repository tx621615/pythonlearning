# string

# string的创建--基本的两种书写方式，三引号的另一种使用方式
str1 = 'Hello World!'
str2 = "Runoob"
str3 = '''a b c
d'''

print(str1, str2, str3)

print("---------")
# 访问字符串
print(str1[0])
print(str1[11])

# 截取字符串  stringname[头：尾] 尾永远是不包括的
print(str1[0:4])
print(str1[0:5])
print(str1[:11])
print(str1[0:])

# 逆序打印---尾字符为-1起始
print(str1[:-1])  # Hello World
print(str1[2:-1])  # llo World
print(str1[-12:])  # Hello World!

# 多个重复字符串打印
print(str1 * 2)

# 连接字符串 +
print("test " + str1)

'''
    常用转义字符
        1. \n
        2. \\
        3. \'
        4. \"
        5. \t
'''

'''
    注意python里没有char,char == 一个字符的字符串
'''
# in / not in成员字符串
if 'a' in str1:
    print('a在 Hello World! 中')
else:
    print('a不在 Hello World! 中')   # a不在 Hello World! 中

if 'Hello' in str1:
    print('Hello 在 str1中')
else:
    print('Hello 不在 str1中')  # Hello 在 str1中

# 格式化字符串的作用用于动态改变字符串的值
'''
    常用格式化函数: %s, %d
'''
print('我叫%s, 今年%d岁' %('tangxin', 24))

# 直接使用格式化字符串
# 替换变量
name = 'tangxin'
str2 = f'我叫 {name}'
age = 24
str3 = f', 今年 {age}了！'
print(str2 + str3)
# 替换表达式
str3 = f'{str2 + str3}'
print(str3)
str4 = f'{1 + 2}'
print(str4)