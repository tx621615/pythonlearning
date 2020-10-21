# end关键字
# Fibo数列，前两项和为第三项的值
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a + b