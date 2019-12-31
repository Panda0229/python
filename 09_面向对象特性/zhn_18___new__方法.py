class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):

        # 创建对象时，ｎｅｗ方法会被自动调用
        print("创建对象分配空间")

        # 为对象分配空间
        instance = super().__new__(cls)

        # 返回对象引用
        return instance

    def __init__(self):

        print("播放器初始化")


# 创建播放器对象
player = MusicPlayer()

print(player)

# 重写 __new__ 方法 一定要 return super().__new__(cls)
# 否则 Python 的解释器 得不到 分配了空间的 对象引用，就不会调用对象的初始化方法
# 注意：__new__ 是一个静态方法，在调用时需要 主动传递 cls 参数
