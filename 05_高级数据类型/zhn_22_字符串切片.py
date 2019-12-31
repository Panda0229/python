num_str = "0123456789"
print(num_str)
# 截取从2到5位置的字符
print(num_str[2:6])
# 截取2到末尾的字符串
print(num_str[2:])
# 截取完整的字符串
print(num_str[:])
# 从开始位置，每隔一个字符截取字符串
print(num_str[::2])
# 从索引1开始，每隔一个取一个
print(num_str[1::2])
# 截取从2到末尾-1的字符串,-1是倒数第一个字符
print(num_str[2:-1])
# 截取字符串末尾两个字符
print(num_str[-2:])
# 字符串逆序
print(num_str[-1::-1])