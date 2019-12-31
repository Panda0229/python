xiaoming = {"name":"xiaoming","age":45}

# 统计键值对数量
print(len(xiaoming))

# 合并字典
temp = {"height":123}
xiaoming.update(temp)
# 如果被合并字典中存在已有键值对，则覆盖原有键值对

# 清空字典
xiaoming.clear()




print(xiaoming)