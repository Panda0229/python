# 打开文件
file = open("README")

# 读取文件内容
text = file.read()
print(text)
print(len(text))

print("-" * 50)

text = file.read()
print(text)
print(len(text))

# 关闭文件
file.close()


# 文件指针 标记 从哪个位置开始读取数据
# 第一次打开 文件时，通常 文件指针会指向文件的开始位置
# 当执行了 read 方法后，文件指针 会移动到 读取内容的末尾
# 默认情况下会移动到 文件末尾
# 文件指针移动到了文件末尾，再次调用不会读取到任何的内容