class Cat:
    def __init__(self):

        print("这是一个初始化方发")

        # self.属性名 = 属性的初始值
        self.name = "Tom"

    def eat(self):
        print("%s爱吃鱼"%self.name)


# 使用类名（）创建对象的时候，会自动调用初始化方法__init__。
tom = Cat()
tom.eat()

print(tom.name)