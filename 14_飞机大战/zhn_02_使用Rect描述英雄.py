# - pygame.Rect 是一个比较特殊的类，内部只是封装了一些数字计算
# - 不执行 pygame.init() 方法同样能够直接使用

import pygame

hero_rect = pygame.Rect(100, 500, 120, 125)

print("英雄的原点 %d %d" % (hero_rect.x, hero_rect.y))
print("英雄的尺寸　%d %d" % (hero_rect.width, hero_rect.height))
print("%d %d" % hero_rect.size)


# - 在游戏中，所有可见的元素 都是以 矩形区域 来描述位置的
#   - 要描述一个矩形区域有四个要素：(x, y) (width, height)
# - pygame 专门提供了一个类 pygame.Rect 用于描述 矩形区域
#
#     Rect(x, y, width, height) -> Rect
# 执行Rect函数会返回一个元祖，用Rect类的size方法表示


