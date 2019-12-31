import pygame
from plane_sprites import *
# import导入模块使用时必须要模块.的方法，from导入时可以
# 直接使用模块的工具，而不用输入模块的名称

# 一、游戏初始化
pygame.init()

# 创建游戏窗口 480*700
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
bg = pygame.image.load("./images/background.png")
screen.blit(bg,(0, 0))
# pygame.display.update()

# 调用英雄的飞机图片
hero = pygame.image.load("./images/me1.png")

# 可以再所有绘制工作完成之后，统一调用update方法
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 1 定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)  # 英雄飞机坐标的元祖


# 创建敌机的精灵
enemy = GameSprit("./images/enemy1.png")
enemy1 = GameSprit("./images/enemy1.png", 2)
# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)


# 二、游戏循环，意味着游戏的正式开始
while True:

    # 可以指定循环体内部代码执行的帧率
    clock.tick(60)

    # 监听事件
    for event in pygame.event.get():

        # 判断时间类型是否是推出事件
        if event.type == pygame.QUIT:  # type事件属性返回发生的事件的类型，即当前 Event对象表示的事件的名称。
            print("游戏退出")

            # 调用quit卸载所有模块
            pygame.quit()

            # 调用exit，直接终止当前执行的程序。ｂｒｅａｋ是退出循环。所以不用
            exit()

    # 2　修改飞机的位置
    hero_rect.y -= 1

    # 判断飞机的位置
    if hero_rect.y <= -126:
        hero_rect.y = 700

    # 3 调用blit方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 让精灵组调用两个方法
    # update-让组中的所有精灵更新位置
    enemy_group.update()
    # draw-在screen上绘制所有的精灵
    enemy_group.draw(screen)

    # 4 调用update方法更新显示
    pygame.display.update()


pygame.quit()


