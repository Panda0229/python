def sum_2_num(num1,num2):
    """对两个数字求和"""
    result = num1 + num2
    # 使用返回值告诉调用方结果
    return result
    #return下面的代码不会被执行

# 可以使用变量来接受函数返回结果
a = sum_2_num(10,30)
print("结果是%d"%a)
