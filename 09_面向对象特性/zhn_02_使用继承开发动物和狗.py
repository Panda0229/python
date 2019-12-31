# 继承的概念：子类 拥有 父类 的所有 方法 和 属性


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


wangcai = Dog()

wangcai.eat()
wangcai.sleep()
wangcai.run()
wangcai.drink()
wangcai.bark()


# Dog 类是 Animal 类的子类，Animal 类是 Dog 类的父类，Dog 类从 Animal 类继承
# Dog 类是 Animal 类的派生类，Animal 类是 Dog 类的基类，Dog 类从 Animal 类派生

