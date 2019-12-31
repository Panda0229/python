name_list = ["熊大","熊二","光头强"]

# 1.取值和取索引
print(name_list[0])
# 知道数据在列表中的位置
print(name_list.index("熊大"))
# 2.修改
name_list[1] = "肥波"
# 3.增加,append追加，insert指定位置,extend把另一个加到末尾
name_list.append("熊二")
name_list.insert(2,"吉吉")
temp_list = ["毛毛","壮壮"]
name_list.extend(temp_list)
# 4.删除 remove删除指定数据,pop默认删除列表最后一个数据，也可以制定删除元素的索引
#
name_list.remove("毛毛")
name_list.pop(2)
name_list.clear()
print(name_list)


# 列表可以存储不同类型的数据，大部分情况下都存储相同类型的数据