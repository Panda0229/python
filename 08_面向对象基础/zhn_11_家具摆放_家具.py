# 需求
# 房子(House) 有 户型、总面积 和 家具名称列表
# 新房子没有任何的家具
# 家具(HouseItem) 有 名字 和 占地面积，其中
# 席梦思(bed) 占地 4 平米
# 衣柜(chest) 占地 2 平米
# 餐桌(table) 占地 1.5 平米
# 将以上三件 家具 添加 到 房子 中
# 打印房子时，要求输出：户型、总面积、剩余面积、家具名称列表


class HouseItem:

    def __init__(self, name, area):

        self.name = name
        self.area = area

    def __str__(self):

        return "[%s] 占地 %.2f" % (self.name, self.area)


# 创建家具
bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)
print(bed)
print(chest)
print(table)
