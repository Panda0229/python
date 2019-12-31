xiaoming = {"name":"xiaoming"}
# 取值
print(xiaoming["name"])

# 增加修改 如果key不存在，则新增键值对，如存在，则修改原有键值对
xiaoming["age"] = 18
xiaoming["name"] = "hualala"

# 删除
xiaoming.pop("age")



print(xiaoming)