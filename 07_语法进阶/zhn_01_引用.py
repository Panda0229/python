def test(num):
    print("在函数内部%d对应的内存地址是%d"%(num,id(num)))

    # 定义一个字符串变量
    result = "hello"
    print("函数要返回的数据内存地址是%d"%id(result))
    # 将字符串变量返回
    return result  # 返回数据引用，不是数据本身
# 定义数字变量
a = 10

print("a保存数据的地址是%d"%id(a))
# 数据地址本质上就是数字


# 调用test函数
# 注意，函数有返回值，没有变量接受，不会报错，但是没有返回结果
r = test(a)  # r接受函数返回结果

print("%s的内存地址是%d"%(r,id(r)))

# 调用函数时本质是传递实参保存数据的引用，而不是实参数据