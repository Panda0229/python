# 1. 定义一个函数 sum_numbers
# 2. 能够接收一个 num 的整数参数
# 3. 计算 1 + 2 + ... num 的结果


def sum_number(num):

    # 出口
    if num == 1:
        return 1

    # 数字累加num+（1+。。。+num—1）
    # 假设sun_number能够处理1...num-1
    temp = sum_number(num-1)

    return num+temp


result = sum_number(5)
print(result)

