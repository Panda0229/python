class A:

    def test(self):
        print("test A 方法")

    def demo(self):
        print("demo A 方法")


class B:

    def demo(self):
        print("demo B 方法")

    def test(self):
        print("test B 方法")


class C(A,B):
    """多继承可以让子类的对象同时具有多个父类的属性和方法"""
    pass

# 提示：开发时，应该尽量避免这种容易产生混淆的情况！
# —— 如果 父类之间 存在 同名的属性或者方法，应该 尽量避免 使用多继承
# 创建子类对象
c = C()
c.test()
c.demo()

# 确定Ｃ类对象调用方法的顺序

print(C.__mro__)  # MRO是method resolution order，主要用于在多继承时判断方法、属性的调用路径
