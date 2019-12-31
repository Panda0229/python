for num in [1,2,3,4]:
    print(num)
    if num == 2:
        break
# 如果循环体内部使用了break循环，则else不会被执行
else:
    print("山炮")
print("循环结束")