# 关于 super
# 在 Python中super是一个特殊的类
# super()就是使用super类创建出来的对象
# 最常使用的场景就是在重写父类方法时，调用在父类中封装的方法实现


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
        # １　针对子类特有的需求编写代码
        print("神叫")

        # 2 使用super(),调用原本在父类中封装的方法
        super().bark()

        # 3 增加其他子类代码
        print("!@##$$%%^^&&()")


xtq = xiaotian()
xtq.bark()


