name_list = ["熊大","熊二","光头强","熊大"]
# 使用迭代遍历列表
"""
顺序的从列表中依次获取数据，每一次循环中，数据都会保存在 name 这个变量中，在循环体内部可以
访问到当前这次获取到的数据
for name in 列表变量:
    print("我的名字叫%s"%name)
"""
for name in name_list:
    print("我的名字叫%s"%name)