str = "hello world"

# 判断是否以指定字符串开始
print(str.startswith("hello"))

# 判断是否以指定字符串结束
print(str.endswith("hello"))

# 查找指定字符串,字符串不存在会返回 -1，而index则会报错
print(str.find("wo"))
print(str.find("ab"))
# 替换字符串,会输出新的字符串，不会修改原有字符串
print(str.replace("wo","haha"))

print(str)