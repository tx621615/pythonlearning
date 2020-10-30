"""
命名空间和作用域

1.命名空间：通过python字典表示---内置，全局（模块），局部
2.作用域：
    一个变量名/或者函数名等查找命名空间的顺序---- L --- E ---- G ---- Built-in
    查找顺序变相说明了其作用域---类似一个树结构  builtin为跟节点，全局变量为子节点，局部变量为孙节点，局部的局部。。。，所有变量可以作用与该域和其子孙节点的域
    （Local）：最内层，包含局部变量，比如一个函数/方法内部。
    E（Enclosing）：包含了非局部(non-local)也非全局(non-global)的变量。比如两个嵌套函数，一个函数（或类） A 里面又包含了一个函数 B ，那么对于 B 中的名称来说 A 中的作用域就为 nonlocal。
    G（Global）：当前脚本的最外层，比如当前模块的全局变量。
    B（Built-in）： 包含了内建的变量/关键字等。，最后被搜索

3.Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，
也就是说这些语句内定义的变量，外部也可以访问。 --- 其实就是全局作用域

总结：
    1.注意作用域可以用在本身和下级作用域
    2.变量查找顺序，局部可以掩盖全局
    3.如何在局部改变全局变量而非重新定义
    4.if,for,while等块定义的变量为全局而非局部
"""

# 验证if 块所定义的变量为全局作用域
if True:
    msg = 'I am a global variable.'
print(msg)

# 验证for中定义的变量
for i in range(9):
    pass
print(i)

# 全局变量和局部变量--内部作用域想要修改外部作用域的值
total = 0


def sum(n1, n2):
    total = n1 + n2   # 这里其实是一个定义语句，即重新定义了函数内的局部变量total，尽量避免该写法
    print("函数内局部变量：", total)
    return total


sum(10, 20)
print("全局变量", total)


# 避免使用定义局部变量语句而转化为赋值语句Global/ nonlocal

num = 1


def func1():
    global num  # 声明使用num指的是全局变量
    print(num)
    num = 123  # 将其解释为赋值而非定义局部变量
    print(num)


func1()
print(num)


def outer():
    n = 0
    def inner():
        nonlocal n
        n = 100
        print(n)
    inner()
    print(n)

outer()


a = 10
def test(a):
    a = a + 1  # 此时a为局部变量
    print(a)
