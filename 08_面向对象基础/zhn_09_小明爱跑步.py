class Person:

    def __init__(self, name, weight):

        # 等号右侧为形参，左侧为属性，self.属性 = 形参
        self.name = name
        self.weight = weight

    def __str__(self):
        #  %2f小数点后面两位小数
        return "我的名字是%s,体重是%.2f公斤" % (self.name, self.weight)

    def run(self):
        print("%s 爱跑步" % self.name)
        self.weight -= 0.5

    def eat(self):
        print("%s 吃饭" % self.name)
        self.weight += 1


xiaoming = Person("小明", 75.0)

xiaoming.run()
xiaoming.eat()

print(xiaoming)

