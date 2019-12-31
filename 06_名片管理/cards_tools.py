# 记录所有的名字字典
card_list = []


def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】V1.0")
    print("")
    print("1.新增名片")
    print("2.显示全部")
    print("3.搜索名片")
    print("")
    print("0.退出系统")
    print("*" * 50)


def new_card():
    """新增名片"""
    print("-" * 50)
    print("新增名片")
    # 提示用户输入详细名片信息
    name_str = input("请输入姓名： ")
    phone_str = input("请输入电话： ")
    email_str = input("请输入邮箱地址： ")
    qq_str = input("请输入qq号码： ")
    # 使用用户输入的信息建立一个名片字典
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "QQ": qq_str,
                 "email": email_str}
    # 将名片字典添加到列表中
    card_list.append(card_dict)
    print(card_list)
    # 提示用户添加成功
    print("添加%s的名片添加成功" % name_str)


def show_all():
    """显示所有名片"""
    print("-" * 50)
    print("显示所有名片")
    # 判断是否存在名片记录，如果没有，提示用户并返回
    if len(card_list) == 0:
        print("当前没有记录，请增加名片！！")
        # return可以返回一个函数的执行结果，并且下方的代码不会被执行
        # 如果return后面没有任何的内容，表示会返回到添加函数的位置，
        # 并且不会返回任何为结果
        return

    # 打印表头
    for name in ["姓名", "电话", "qq", "邮箱"]:
        print(name, end="\t\t")  # 水平制表符
    print("")

    # 打印分割线
    print("=" * 50)
    # 遍历名片列表一次输出字典信息
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["QQ"],
                                        card_dict["email"]))


def search_card():
    """搜索名片"""
    print("-" * 50)
    print("搜索名片")
    # 提示用户输入要搜索的姓名，
    find_name = input("请输入要搜索的姓名： ")

    # 遍历名片列表，查询要搜索的姓名，如果没有找到，需要提示用户
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱\t\t")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["QQ"],
                                            card_dict["email"]))
            # TODO 针对找到的名片记录执行修改和删除的操作
            deal_card(card_dict)
            break
    else:
        print("没找到%s" % find_name)


def deal_card(find_dict):
    print(find_dict)
    action_str = input("请输入对名片的操作：1: 修改/ 2: 删除/ 0: 返回上级菜单")
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "姓名：")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话：")
        find_dict["QQ"] = input_card_info(find_dict["QQ"], "QQ: ")
        find_dict["email"] = input_card_info(find_dict["email"], "email: ")
        print("修改名片成功")
    elif action_str == "2":
        card_list.remove(find_dict)
        print("删除名片成功")

def input_card_info(dict_value,tip_message):
    # 提示用户输入内容
    result_str = input(tip_message)
    # 针对用户的输入进行判断，如果用户输入了内容，直接返回结果
    if len(result_str) > 0:
        return result_str
    # 如果用户没有输入内容，返回字典中原有的值
    else:
        return dict_value
