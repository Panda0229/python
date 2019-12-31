# 必须保证带有默认值的缺省参数在参数列表末尾
def print_info(name,title="",gender=True):  # gender是缺省参数，默认值为True
    """

        :param title: 职位
        :param name: 班上同学姓名
        :param gender: true男生，False女生
        """

    gender_text = "男生"
    if not gender:
        gender_text = "女生"

    print("[%s]%s是%s"%(title, name, gender_text))


# 假设班上同学男生居多
# 在指定缺省参数默认值时，应该使用最常见的值作为默认值
print_info("小明")
print_info("熊大")
# 在调用函数时，如果有多个缺省参数，需要指定参数名，
# 这样解释器才能够知道参数的对应关系！
print_info("水冰月", gender=False)

