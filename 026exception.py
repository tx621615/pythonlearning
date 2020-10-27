# 异常处理
"""
异常处理格式：
try:
<语句>        #运行别的代码
except <名字>：
<语句>        #如果在try部份引发了'name'异常
except <名字>，<数据>:
<语句>        #如果引发了'name'异常，获得附加的数据
else:
<语句>        #如果没有异常发生

1.如果当try后的语句执行时发生异常，python就跳回到try并执行第一个匹配该异常的except子句，异常处理完毕，控制流就通过整个try语句（除非在处理异常时又引发新的异常）。
2.如果在try后的语句里发生了异常，却没有匹配的except子句，异常将被递交到上层的try，或者到程序的最上层（这样将结束程序，并打印默认的出错信息）。
3.如果在try子句执行时没有发生异常，python将执行else语句后的语句（如果有else的话），然后控制流通过整个try语句。

捕获多种异常
try:
    正常的操作
   ......................
except(Exception1[, Exception2[,...ExceptionN]]]):
   发生以上多个异常中的一个，执行这块代码
   ......................
else:
    如果没有异常执行这块代码

捕获所有异常
try:
    正常的操作
   ......................
except:
    发生异常，执行这块代码
   ......................
else:
    如果没有异常执行这块代码
"""

try:
    f = open("testfile", "r")
    f.read()
except IOError:
    print("Error: 没有该文件")
else:
    print("内容可读")
    f.close()

# try finally--finally语句在try块退出时必定执行，try嵌套--内存出错异常交给外层try处理
try:
    fh = open("testfile", "r")
    try:
        fh.read()
    finally:
        print("关闭文件")
        fh.close()
except IOError:
    print("Error: 没有找到文件或读取文件失败")

# raise主动触发异常
# raise [Exception [, args[,traceback]]]
# 定义异常实例（except MyError as e）


def not_zero(num):
    try:
        if num == 0:
            raise ValueError("参数错误")
        return num
    except Exception as e:
        print(e)


not_zero(0)

# 自定义异常类,一般继承自Exception,所有内置异常基类确实BaseException


class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    raise MyError('类型错误')
except MyError as e:
    print(e)




