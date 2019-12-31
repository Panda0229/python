# 将字符串中空白字符去掉，在使用“ ”作为分割符，拼接成一个整齐的字符串
poem_str = "叽里咕噜\t唏哩呼噜\n幽默是专业的行为艺术\t\n就算是跟猫打招呼" \
           "\t或者是跟狗问路也要很专注"
print(poem_str)

# 拆分字符串，split将字符串拆分成字符串的列表

poem_list = poem_str.split()
print(poem_list)

# 合并字符串

poem_str1 = " ".join(poem_list)
print(poem_str1)