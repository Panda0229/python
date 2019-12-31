# 定义整数变量age，判断年龄是否正确，要求人年龄在0——120之间
age = int(input("输入年龄："))
if age >= 0 and age <=120:
    print("right")
else:
    print("error")