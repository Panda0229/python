# 注意 在开发时，应该把模块中所有的全局变量定义在
# 所有函数的上方，就可以保证所有的函数都能正常的访问到每一个全局变量了
num = 10


def demo():
    print("%d"%num)
    print("%s"%title)
  # print("%s"%name)
# 再定义一个全局变量
title = "巴拉拉小魔仙"
demo()

# 再定义一个全局变量
# name = "阿童木"