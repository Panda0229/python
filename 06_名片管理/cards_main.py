#! /usr/bin/python3
# 上一句注释表示将程序变为可执行程序

import  cards_tools
# 无限循环，有用户决定什么时候退出操作
while True:
    # TODO（括号里面为应做这项工作的人名字） 显示功能菜单（做完工作可以删掉）
    cards_tools.show_menu()

    action_str = input("选择希望执行的操作：")  # 输入并不转换成int型
    print("您选择的操作是[%s]"%action_str)

    # 1.2.3针对名片操作,不希望立刻编写分支内部代码时，暂时用pass代替，
    # pass是一个站位符，可以保证代码结构正确，程序运行时，pass不会执行任何操作
    if action_str in ["1","2","3"]:  # 判断时直接针对字符串进行判断
        # 新增名片
        if action_str == "1":
            cards_tools.new_card()
        # 显示全部
        elif action_str == "2":
            cards_tools.show_all()
        # 查询名片
        elif action_str == "3":
            cards_tools.search_card()

    # 0退出系统
    elif action_str == "0":
        print("欢迎再来[名片管理系统]")
        break
    # 其他内容输入错误，需要提示用户
    else:
        print("不对，滚，重来")
