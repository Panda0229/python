# 当 Python 解释器 抛出异常 时，最后一行错误信息的第一个单词，就是错误类型
try:
    # 提示用户输入一个整数0
    num = int(input("输入一个整数："))

    # 使用８除以用户输入的整数并输出
    result = 8 / num

    print(result)

except ZeroDivisionError:
    print("除０错误")

except ValueError:
    print("请输入正确的整数")

