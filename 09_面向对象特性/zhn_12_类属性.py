class Tool(object):

    # 使用赋值语句定义类属性，记录所有工具的数量
    count = 0

    def __init__(self, name):
        self.name = name

        # 让类属性值＋１
        Tool.count += 1


# 创建工具对象
tool_1 = Tool("斧头")
tool_2 = Tool("榔头")
tool_3 = Tool("水桶")
# 输出工具对象的总数
print(Tool.count)
