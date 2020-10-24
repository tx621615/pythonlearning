"""
总结：
1.定义function:
    def functionname(parameter-list)
        function-body
2.return 语句可有可无，因为没有返回类型
3.函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
4.可变长参数--使用的是元组
5.匿名函数:lambda表达式
"""

# python中类型属于对象，而引用（变量）没有类型

# 不定长参数,
'''
    1.用*号表示，传入的参数会被送入元组中
    def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
   
   2.用**表示，表示传入key-value对到字典变量中
   def functionname([formal_args,] **var_args_dict ):
   "函数_文档字符串"
   function_suite
   return [expression]
   
'''

# 用元组接收不定长参数


def printinfo(arg1, *vartuple):
    """打印任何传入的参数"""
    print("输出：")
    print(arg1)
    print(vartuple)


printinfo(2, 50, 60)


# 用字典接受参数


def printinfo(arg1, **vardic):
    """打印任何传入的参数"""
    print("输出:")
    print(arg1)
    print(vardic)


# 少用，不懂什么意思
printinfo(2, a=2, b=3)

# 匿名函数--采用Lambda表达式

"""
python 使用 lambda 来创建匿名函数。
所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
1.lambda 只是一个表达式，函数体比 def 简单很多。 
2.lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。 
3.lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
4.lambda匿名函数的格式：冒号前是参数，可以有多个，用逗号隔开，冒号右边的为表达式。其实lambda返回值是一个函数的地址，也就是函数对象。
5.lambda 函数可以接收任意多个参数 (包括可选参数) 并且返回单个表达式的值。
"""

# lambda表达式返回函数地址，其实就是无名函数，同时返回当个表达式的值。
sum = lambda x, y: x + y
print(sum(5, 6))


