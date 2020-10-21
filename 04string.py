'''String 类型的使用
1.python中没有char,一个char就是一个字符的字符串
2.python中单引号和双引号都可以表示字符串
3.多行字符串可以用三引号（单双都可以）表示
4.索引：左到右0开始，右到左-1开始
5.反转义r""会使字符串中转义字符打出而不生效
6.string的截取str[头下标：尾下标：步长] 不包括尾下标
7.string拼接---+, string重复----*
'''

str = 'Runoob'

print(str)   #print除了打印相关内容还会默认换行
print(str[0:-1]) #不包括尾下标的元素
print(str[0])   
print(str[2:5])
print(str[2:])  #打印从2后所有内容
print(str * 2)  #重复
print(str + '你好')
print('------------------------')
print(str[0::2]) #打印相隔k的下标的字符

print('------------------------')

print('hello\nrunoob')
print(r'hello\nrunnob')

print('------------------------')
#多行字符
str1 = '''I'm
tangxin'''
print(str1) #多行字符的格式也会打印出来（编辑器上什么格式终端上什么格式）

