# 判断空白字符和空格，空白字符是指转义字符
space_str = "   \t\n\r"
print(space_str.isspace())
# 判断是否只包含数字
# 三者均不可判断小数，\u00b2为平方
#num_str = "1.1"
# num_str = "\u00b2"
# num_str = "(1)"
num_str = "一"

print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())