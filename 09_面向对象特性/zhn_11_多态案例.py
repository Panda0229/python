class Dog(object):  # 今后在定义类时，如果没有父类，建议统一继承自object

    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 哈士奇拆家式玩耍。。" % self.name)


class XiaoTianDog(Dog):

    def game(self):
        print("%s 飞啊飞啊我的骄傲放纵" % self.name)


class Person(object):

    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s 和 %s一起快乐的拆家" % (self.name, dog.name))

        # 让狗玩耍
        dog.game()


# 创建一个狗对象
wangcai = Dog("旺财")

wangcai = XiaoTianDog("飞天旺财")

# 创建一个小明对象
xiaoming = Person("小明")

# 让小明调用和狗玩的方法
xiaoming.game_with_dog(wangcai)