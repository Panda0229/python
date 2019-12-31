name_list = ["熊大","熊二","光头强"]

# 使用del删除列表元素
del name_list[1]

# del 关键字本质上是用来将一个变量从内存中删除,后续的代码不能再引用此变量，少用

name = "毛毛"
del name

print(name_list)