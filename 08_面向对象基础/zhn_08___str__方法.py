class Cat:
    def __init__(self, new_name):

        self.name = new_name

        print("%s来了" % self.name)

    def __del__(self):
        print("%s 我走了" % self.name)

    def __str__(self):  # 是print函数打印自定义的信息
        # 必须返回一个字符串
        return ("我是一只猫%s" % self.name)

# tom是一个全局变量
tom = Cat("tom")
print(tom)