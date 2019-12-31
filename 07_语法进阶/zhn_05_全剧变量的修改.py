num = 10  # 全剧变量


def demo1():
    # 希望修改全剧变量的值。可以用global声明以下即可
    # global关键字会告诉解释器后面的变量是一个全剧变量，再使用
    # 赋值语句时，不会创建局部变量
    global num
    num = 99
    print("demo1 == %d"%num)



def demo2():
    print("demo2 == %d" % num)


demo1()
demo2()
