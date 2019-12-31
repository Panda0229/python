"""
输入苹果单价
输入苹果数量
计算苹果金额
"""
price_str = input("苹果的单价: ")
weight_str = input("苹果的重量:  ")  # 两个字符串之间不能执行乘法
price = float (price_str)
weight = float (weight_str)
money = price * weight
print(money)