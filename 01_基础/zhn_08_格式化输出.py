# 定义字符变量 name 输出 我的名字叫小明
name = "山炮"
print("我的名字叫%s"%name)
student_number = 110123456
print("我的学号是%03d"%student_number)
#买苹果
price = float(input("苹果的单价 "))
weight = float(input("苹果的重量 "))
money = price * weight
print("苹果单价%.2f,苹果重量%.2f,需要支付%.44f"%(price,weight,money))
#定义一个小数，输出数据比例是10.00%
scale = 0.25
print("输出数据比例是%f%%"%(scale * 100))