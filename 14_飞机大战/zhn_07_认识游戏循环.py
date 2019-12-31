import pygame

# 一、游戏初始化
pygame.init()

# 创建游戏窗口 480*700
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
bg = pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))
# pygame.display.update()

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero,(200,500))
# 可以再所有绘制工作完成之后，统一调用update方法
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()


# 二、游戏循环，意味着游戏的正式开始
while True:
    # 可以指定循环体内部代码执行的帧率
    clock.tick(60)
    pass

pygame.quit()


