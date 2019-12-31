class Game(object):

    # 历史最高分
    top_store = 0

    def __init__(self, player_name):

        self.player_name = player_name

    @staticmethod
    def show_help():
        print("帮助信息：哗啦啦")

    @classmethod
    def show_top_score(cls):
        print("历史记录：%d" % cls.top_store)

    def start_game(self):
        print("%s 开始游戏" % self.player_name)


# 查看游戏帮助信息
Game.show_help()

# 查看历史最高分
Game.show_top_score()

# 创建游戏对象
game = Game("小明")

game.start_game()


# 实例方法 —— 方法内部需要访问 实例属性
# 实例方法 内部可以使用 类名. 访问类属性
# 类方法 —— 方法内部 只 需要访问 类属性
# 静态方法 —— 方法内部，不需要访问 实例属性 和 类属性
# 提问
# 如果方法内部即需要访问实例属性，又需要访问类属性，应该定义成什么方法？
# 答案
# 应该定义实例方法
# 因为，类只有一个，在实例方法内部可以使用类名. 访问类属性

