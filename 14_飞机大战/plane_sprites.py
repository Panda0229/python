import random
import pygame
# 在导入模块时，建议 按照以下顺序导入
# 1. 官方标准模块导入
# 2. 第三方模块导入
# 3. 应用程序模块导入

# 定义屏幕大小的常量
# 常量 的 命名 应该 所有字母都使用大写，单词与单词之间使用下划线连接
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量,pygame.USEREVENT是pygme提供的用户常量，是一个整数
CREAT_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹事件
HERO_FIRE_EVET = pygame.USEREVENT + 1


class GameSprit(pygame.sprite.Sprite):  # 第一个sprite是模块名称，第二个Sprite是类名称
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):

        # 调用父类的初始化方法
        super().__init__()
        # 定义对象属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):

        # 在屏幕垂直方向移动
        self.rect.y += self.speed

# 注意
# - 如果一个类的父类不是object
# - 在重写初始化方法时，一定要先super()一下父类的__init__方法
# - 保证父类中实现的__init__代码能够被正常执行


class Background(GameSprit):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):

        # 1 调用父类方法实现精灵的创建（image/rect/speed）
        super().__init__("./images/background.png")
        # 2 判断是否是交替图像，如果是，需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):

        # １调用父类方法实现
        super().update()

        # 2 判断是否移出屏幕，如果移出屏幕，将图像设置到屏幕的正上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprit):
    """敌机精灵"""
    def __init__(self):

        # 调用父类方法创建敌机精灵，同时制定敌机图片
        super().__init__("./images/enemy1.png")
        # 指定敌机的初始随机速度 1~3
        self.speed = random.randint(1, 3)
        # 指定敌机的初始随机位置
        # - bottom = y + height
        # - y = bottom - height

        self.rect.bottom = 0

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(1, max_x)

    def update(self):

        # 调用父类方法，保持垂直方向飞行
        super().update()
        # 判断是否飞出屏幕，如果是，需要从精灵族删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            # print("飞出屏幕，需要从精灵组删除")
            # kill方法可以将精灵从所有精灵组中移出，精灵就会被自动销毁
            self.kill()

    # __del__是内置方法会在对象被销毁前调用，在开发中，可以用于判断对象是否被销毁
    def __del__(self):
        # print("敌机挂了%s " % self.rect)
        pass


class Hero(GameSprit):
    """英雄精灵"""
    def __init__(self):

        # 1 调用父类方法，设置image,speed
        super().__init__("./images/me1.png", 0)
        # 2 设置英雄初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        # 创建子弹的精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):

        # 英雄在水平方向移动
        self.rect.x += self.speed

        # 控制英雄不能离开屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        # right = x + width 利用 right 属性可以非常容易的针对右侧设置精灵位置
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        print("发射子弹")

        for i in (0, 1, 2):
            # 1创建子弹精灵
            bullet = Bullet()

            # 2设置精灵位置
            bullet.rect.bottom = self.rect.y - i *  20
            bullet.rect.centerx = self.rect.centerx

            # 3将精灵添加到精灵组
            self.bullets.add(bullet)

class Bullet(GameSprit):
    """子弹精灵"""

    def __init__(self):

        # 调用父类方法，设置子弹图片，设置子弹速度
       super().__init__("./images/bullet1.png", -2)

    def update(self):

        # 调用父类方法，让子弹沿垂直方向飞行
        super().update()

        # 判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()


    def __del__(self):
       print("子弹挂了")
