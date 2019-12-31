# 定义布尔型变量 has_ticket 表示是否有车票
has_ticket = True
# 定义整型变量 knife_length 表示刀的长度，单位：厘米
knife_length = 2
# 首先检查是否有车票，如果有，才允许进行 安检
if has_ticket:
    print("pass,进安检")
# 安检时，需要检查刀的长度，判断是否超过 20 厘米
    if knife_length > 20:
        print("刀长有%d,滚！"%knife_length)
# 如果超过 20 厘米，提示刀的长度，不允许上车
# 如果不超过 20 厘米，安检通过
    else:
        print("pass")
# 如果没有车票，不允许进门
else:
    print("滚！")