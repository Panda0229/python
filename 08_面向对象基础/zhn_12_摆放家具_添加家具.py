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

        return "[%s] 占地 %.2f"%(self.name, self.area)


class House:

    def __init__(self, house_table, area):
        self.house_table = house_table
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具列表名称
        self.item_list = []

    def __str__(self):
        return ("户型：%s\n总面积：%.2f[剩余：%.2f]\n家具：%s"
                %(self.house_table, self.area,
                  self.free_area, self.item_list))

    def add_item(self, item):

        print("要添加 %s" % item)
        # 1 判断家具面积
        if item.area > self.free_area:
            print("%s 面积太大，添加不了"%item.name)

            return

        # 2 将家具名称添加到列表中
        self.item_list.append(item.name)
        # 3 计算剩余面积
        self.free_area -= item.area


# 创建家具
bed = HouseItem("席梦思",400)
chest = HouseItem("衣柜",2)
table = HouseItem("餐桌",1.5)
print(bed)
print(chest)
print(table)

# 创建房子对象
my_houme = House("两室一厅",60)

my_houme.add_item(bed)
my_houme.add_item(chest)
my_houme.add_item(table)

print(my_houme)
