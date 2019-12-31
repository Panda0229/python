name_list = ["熊大","熊二","光头强","熊大"]
# len可以统计列表中元素的总数
list_len = len(name_list)
print("列表中元素个数%d"%list_len)
# count可以统计列表中某一个数据出现的次数
count = name_list.count("熊大")
print("熊大出现了%d次"%count)
name_list.remove("熊大")
print(name_list)