# center顺序居中对齐,ljust左对齐，rjust右对齐
poem = ["登鹳雀楼",
        "王之涣",
    "白日依山尽",
    "黄河入海流",
    "欲穷千里目",
    "更上一层楼"]
for poem_str in poem:
    print("|%s|"%poem_str.rjust(10," "))