def demo1():
    #  定义一个局部变量
    # num变量在执行了下方的代码之后，才会被创建
    # 当函数执行完成之后，函数消失
    num = 10
    print ("在demo1函数内部的变量是%d"%num)

def demo2():
    num = 20  # 不同函数内定义的相同的变量彼此之间没有影响
    print("%d"%num)

# 在函数内部定义的变量，不能在其他位置使用
# print("%d"%num)
demo1()
demo2()