a = 6
b = 100

# 解法一，使用其他变量
# c = a
# a = b
# b = c
#
# print(a)
# print(b)

# 解法二，不使用其他变量
# a = a + b
# b = a - b
# a = a - b
#
# print(a)
# print(b)

# 解法三，元祖，python专有,多个变量接收元祖
# a,b = (b,a)
a,b = b,a  # 提示 等号右边是元祖，小括号可以省略

print(a)
print(b)