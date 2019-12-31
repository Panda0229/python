import pygame

pygame.init()

# 创建游戏窗口 480*700
screen = pygame.display.set_mode((480, 700))

while True:
    pass

pygame.quit()

# - pygame 专门提供了一个 模块 pygame.display 用于创建、管理 游戏窗口
#
#   方法                       	说明
#   pygame.display.set_mode()	初始化游戏显示窗口
#   pygame.display.update()  	刷新屏幕内容显示，稍后使用

# set_mode(resolution=(0,0), flags=0, depth=0) -> Surface
# - resolution 指定屏幕的 宽 和 高，默认创建的窗口大小和屏幕大小一致
# - flags 参数指定屏幕的附加选项，例如是否全屏等等，默认不需要传递
# - depth 参数表示颜色的位数，默认自动匹配


