def print_info(name,gender=True):  # gender是缺省参数，默认值为True
    """

        :param name: 班上同学姓名
        :param gender: true男生，False女生
        """

    gender_text = "男生"
    if not gender:
        gender_text = "女生"

    print("%s是%s"%(name,gender_text))


# 假设班上同学男生居多
# 在指定缺省参数默认值时，应该使用最常见的值作为默认值
print_info("小明")
print_info("熊大")
print_info("水冰月",False)