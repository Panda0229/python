def sum_numbers(*args):

    num = 0

    print(args)
    # 循环遍历
    for n in args:
        num += n
    return num


result = sum_numbers(1, 2, 3, 4, 5, 6)
print(result)


# 不用多值参数时实现程序
#
# def sum_numbers(args):
#
#     num = 0
#
#     print(args)
#     # 循环遍历
#     for n in args:
#         num += n
#     return num
#
#
# result = sum_numbers((1, 2, 3, 4, 5, 6))
# print(result)
