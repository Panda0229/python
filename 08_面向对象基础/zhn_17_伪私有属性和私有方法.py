# 在实际开发中，对象的某些属性或方法可能只希望在对象的内部被使用，而不希望在外部被访问到
# 私有属性就是对象不希望公开的属性
# 私有方法就是对象不希望公开的方法


class Women:

    def __init__(self, name):

        self.name = name
        self.__age = 18  # 在定义属性或方法时，在属性名或者方法名前增加两个下划线，定义的就是私有属性或方法

    def __secret(self):
        print("%s 的年龄是 %d" % (self.name, self.__age))


xiaomei = Women("小美")

# 私有属性和私有方法处理方式：在名称前面加上 _类名 => _类名__名称

print(xiaomei._Women__age)


xiaomei._Women__secret()

