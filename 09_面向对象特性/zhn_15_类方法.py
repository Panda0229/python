class Tool(object):

    # 使用赋值语句定义类属性，记录所有工具的数量
    count = 0

    # 定义类方法
    @classmethod
    def show_tool_count(cls):
        print("工具对象的数量　%d " % cls.count)

    def __init__(self, name):
        self.name = name

        # 让类属性值＋１
        Tool.count += 1


# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("水桶")

# 调用类方法
Tool.show_tool_count()

