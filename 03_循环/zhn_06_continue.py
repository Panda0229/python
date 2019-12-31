i = 0
while i < 10:
    i += 1
    if i == 3:
        # 注意，在循环中使用continue，使用关键字之前确认计数是否更改，否则可能导致死循环
        continue
    print(i)

print("over")