# 模块可以向外界提供全局变量、函数、类，注意，直接执行的代码不是向外界提供的工具！


# sayhello函数为模块测试函数，在模块被调用时并不希望执行此函数
# __name__ 属性可以做到，测试模块的代码只在测试情况下被运行，而在被导入时不会被执行！
def say_hello():
    print("你好，我是ｓａｙｈｅｌｌｏ")


# 如果直接执行，输出永远是__main__
# 如果 是被其他文件导入的，__name__ 就是 模块名
# 如果 是当前执行的程序 __name__ 是 __main__
if __name__ == "__main__":
    print(__name__)

    # 文件被导入时，能够直接执行的代码不需要被执行！

    say_hello()
print("小明开发的模块")
