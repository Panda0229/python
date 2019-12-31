class Animal:
    # 父类
    def eat(self):
        print("吃---")

    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")


class Dog(Animal):
    # 子类
    def bark(self):
        print("叫")


class xiaotian(Dog):
    def fly(self):
        print("飞")

    def bark(self):
        print("神叫")

    # 如果在开发中，父类的方法实现和子类的方法实现，完全不同就可以使用
    # 覆盖的方式，在子类中重新编写父类的方法实现


xtq = xiaotian()
# 如果子类中重写了父类方法，在使用子类对象调用方法
#　时，不会调用父类的使用方法
xtq.bark()

