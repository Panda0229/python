row = 1  # 行
while row <= 5:
    col = 1  # 列
    while col <= row:
        # print("%d"%col)
        print("*",end="")
        col += 1
    #print("第%d行"%row)
    print("")  #在每行输出后加上换行
    row += 1