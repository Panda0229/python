def mutiple_table():

    row = 1  # 行
    while row <= 9:
        col = 1  # 列
        while col <= row:
            a = row * col
            print("%d * %d = %d"%(row,col,a),end="\t")
            col += 1
        print("")  #在每行输出后加上换行
        row += 1