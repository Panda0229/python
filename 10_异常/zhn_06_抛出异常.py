# 定义 input_password 函数，提示用户输入密码
# 如果用户输入长度 < 8，抛出异常
# 如果用户输入长度 >=8，返回输入的密码


def input_password():

    # 提示用户输入密码
    pwd = input("请输入密码：　")

    # 判断密码长度>=8,返回用户输入的密码
    if len(pwd) >= 8:
        return pwd

    # 如果<8，主动跑出异常
    print("主动抛出异常")
    # 创建异常对象 - 可以使用错误信息作为参数
    ex = Exception("密码长度不够")

    # 主动抛出异常
    raise ex


# 提示用户输入密码
try:
    print(input_password())

except Exception as result:
    print(result)


# Python 中提供了一个 Exception 异常类
# 在开发时，如果满足 特定业务需求时，希望 抛出异常，可以：
# 创建 一个 Exception 的 对象
# 使用 raise 关键字 抛出 异常对象

