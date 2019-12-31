students = [
    {"name":"熊大"},
    {"name":"熊二"}
]
# 在学员列表中搜索指定的姓名
find_name = "熊"

for stu in students:

    print(stu)

    if stu["name"] == find_name:

        print("来啦，%s"%find_name)
        # 如果找到则推出循环不再遍历后面的元素
        break
else:  # 没有找到目标时
    print("滚，没有%s"%find_name)


print("循环结束")