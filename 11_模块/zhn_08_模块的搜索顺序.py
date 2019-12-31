import random

# 输出模块所在目录
print(random.__file__)

rand = random.randint(0,10)

print(rand)


# 搜索 当前目录 指定模块名的文件，如果有就直接导入
# 如果没有，再搜索 系统目录
# 在开发时，给文件起名，不要和 系统的模块文件 重名
