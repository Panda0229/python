# 一个对象的 属性 可以是 另外一个类创建的对象
# 需求
# 士兵 许三多 有一把 AK47
# 士兵 可以 开火
# 枪 能够 发射 子弹
# 枪 装填 装填子弹 —— 增加子弹数量
# 假设每个新兵都没有枪


class Gun:

    def __init__(self, modle):
        # 枪的型号
        self.modle = modle

        # 子弹数量
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        # 判断子弹数量
        if self.bullet_count <= 0:
            print("[%s] 没有子弹了，溜溜溜" % self.modle)

            return
        # 发射子弹
        self.bullet_count -= 1

        # 提示发射信息
        print("[%s] 打死你个龟孙... 剩[%d]" % (self.modle, self.bullet_count))


class Solder:
    def __init__(self,name):
        # 新兵姓名
        self.name = name

        # 枪 新兵没有枪，在定义属性时，如果 不知道设置什么初始值，可以设置为 None
        self.gun = None


# 创建枪对象
ak47 = Gun("AK47")

ak47.add_bullet(500)
ak47.shoot()

# 创建许三多
xusanduo = Solder("许三多")

xusanduo.gun = ak47  # 一个对象的 属性 可以是 另外一个类创建的对象

print(xusanduo.gun)

