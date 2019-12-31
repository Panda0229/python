# 创建猫类
class Cat:

    def eat(self):
        print("%s爱吃鱼"%self.name)

    def drink(self):
        print("%s要喝水"%self.name)


# 创建猫对象
tom = Cat()

# 可以使用.属性名，利用赋值语句就可以，但是不推荐使用
tom.name = "狗"


tom.eat()
tom.drink()
print(tom)

# 在创建一个猫对象

lazy_cat = Cat()

lazy_cat.name = "仓鼠"

lazy_cat.eat()
lazy_cat.drink()

print(lazy_cat)

