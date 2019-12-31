class Cat:
    def __init__(self,new_name):

        print("这是一个初始化方发")

        # self.属性名 = 属性的初始值
        # self.name = "Tom"
        self.name = new_name
    def eat(self):
        print("%s 爱吃鱼" % self.name)


# 使用类名（）创建对象的时候，会自动调用初始化方法__init__。不用单独写出
tom = Cat("Tom")
tom.eat()

lazy_cat = Cat("狗")
lazy_cat.eat()