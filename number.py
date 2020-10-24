# number类型有int, float, complex
import random
# 类型转换
a = 1.0
print(int(a))
a = 1
print(float(a))
print(complex(1, 2))  # 复数的表示形式 a + bj

# 随机数random()[0,1)
print(random.random() * 5)