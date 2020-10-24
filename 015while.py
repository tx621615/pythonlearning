# 循环语句while and for

# while简单测试
# 格式化输出1-100和
sum = 0
count = 1
while count <= 100:
    sum += count
    count += 1
print("1-%d的和为%d"%(count - 1, sum))

# while循环使用else语句,while条件判断为false时执行else语句
count = 0
while count < 5:
    print(count, "小于 5")
    count = count + 1
else:
    print(count, "大于等于5")

print("-----------------------------")
# for语句的作用是用于遍历任何一个序列的项目---类似于java中的for each语句----python中forin语句无法使用下标访问元素
languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    print(x)

# range(start=0, stop[,step]) 创建一个整数列表，默认是从0开始,stop不包括stop,step是步长
print("通过range函数创建一个整数列表：", range(5))

for x in range(5):
    print(x)

# 通过range函数和len函数结合形成for的下标遍历。
languages = ["C", "C++", "Perl", "Python"]
for i in range(len(languages)):
    print(languages[i])

# pass语句，空语句类似于java中的;  ----仅起到占位作用

# continue and break使用与java中类似