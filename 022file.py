# 文件的读写---r,w,a,+
# 文件应该看成一连串的连续字符流，看到的换行，实际为\n，整个文本文件就是一个超长的字符串
# 打开文件 file object = open(file_name [, access_mode][, buffering])
# buffering：=0，则不会有寄存；=1，访问文件时会寄存行；>1，表明这就是的寄存 区的缓冲大小；<0，表示寄存区的缓冲大小为系统默认。
f = open("filetest.txt", "w")

f.write("Python是一个非常好的语言。\n是的，的确非常好!!\n")

f.close()

f = open("filetest.txt", "r")

# f.read(size)读取一定数目的数据，size忽略则读取全部数据,同时返回读回来的字符串
s = f.read()
print(s)
f.close()

# f.readline()会从文件中读取单独的一行，每次读到换行符\n为止，当返回一个空字符串时，说明已经读到最后一行
f = open("filetest.txt", "r")
s = f.readline()
print(s)
print("换行符也读取了")  # 距离两行说明换行符也读取了

# f.readlines()将返回该文件中包含的所有行
f = open("filetest.txt", "r")
s = f.readlines()
print(s) # ['Python是一个非常好的语言。\n', '是的，的确非常好!!\n'] 按行返回了一个原始字符串的列表
f.close()

# 另一种迭代file每行的方式
f = open("filetest.txt", "r")
for s in f:
    print(s, end="") # 因为读取的字符串包含\n
f.close()

# f.write（）从头写入字符串，同时返回写入的字符数目
f = open("filetest.txt", "w")

num = f.write("Python是一个非常好的语言。\n是的，的确非常好!!\n")
print(num)
f.close()

# 写入非字符串的内容要先转化为字符串
f = open("filetest.txt", "w")

value = ('www.runoob.com', 14)
s = str(value)
f.write(s)  # 一旦write之前所有内容全部清空
f.close()

# f.tell()返回文件指针的当前位置
# f.seek(offset, from_what) 0表示开头，1表示当前，2表示结尾，将文件指针设置到指定位置
f = open("filetest.txt", "w+")
f.write("fsafasgha")
f.seek(5, 0) # 注意指针位于字符串之间
print(f.read(2))
f.close()

# 从头开始写会把原来文本文件内容全部删除，而从尾部开始写不会删除
f = open("filetest.txt", "a")
f.write("\nadd something in the end")
f.close()