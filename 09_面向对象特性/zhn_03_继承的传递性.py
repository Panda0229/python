
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


wangcai = xiaotian()

wangcai.eat()
wangcai.sleep()
wangcai.run()
wangcai.drink()
wangcai.bark()
wangcai.fly()