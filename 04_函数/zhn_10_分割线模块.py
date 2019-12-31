def print_line(char,num):
    print(char * num)


def print_lines(char,num):
    """打印多行分割线

    :param char: 分割线内容
    :param num: 字符数量
    """
    row = 0
    while row < 5:
        print_line(char,num)
        row += 1


name = "哗啦啦"