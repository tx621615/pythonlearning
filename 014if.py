# if语句测试---if elif else,每个块后面加冒号
age = int(input("请输入你家狗狗的年龄："))
print("")

# 条件不用加扩号

if age < 0:
    print("你在开玩笑吧")
elif age == 1:
    print("相当于14岁的人")
elif age == 2:
    print("相当于22岁的人")
else:
    human = 22 + (age - 2) * 5
    print("对应的人类年龄: ", human)

# 利用列表和字典来精简判断
msgs = {1 : '相当于14岁的人', 2: '相当于22岁的人'}
default = '其他年龄段的人'
msg = msgs.get(age, default)
print(msg)
# 三元运算符
a, b, c = 1, 2, 3
c = a if a > b else b  # 先执行中间判断,相当于C语言的 C？A:B
print(c)