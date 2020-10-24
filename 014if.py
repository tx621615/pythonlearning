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