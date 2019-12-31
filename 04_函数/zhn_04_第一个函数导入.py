# 函数应该先定义在调用

name = "二狗"

# def只是定义，并没有调用，定义函数上面需要有两个空行（包括注释）


def say_hello():
    """打招呼"""
    print("hello 1")
    print("hello 2")
    print("hello 3")

print(name)
# 只有主动调用，函数才会执行
say_hello()

print(name)