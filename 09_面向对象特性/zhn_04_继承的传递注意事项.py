
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


class Cat(Animal):
    def catch(self):
        print("抓")


wangcai = xiaotian()

wangcai.eat()
wangcai.sleep()
wangcai.run()
wangcai.drink()
wangcai.bark()
wangcai.fly()

# wangcai和cat之间没有继承关系

