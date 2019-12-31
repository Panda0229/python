
# 为了避免局部变量和全局变量出现混淆，在定义全局变量时，
# 有些公司会有一些开发要求，例如：
# 全局变量名前应该增加 g_ 或者 gl_ 的前缀
gl_num = 10
# 再定义一个全局变量
gl_title = "巴拉拉小魔仙"
# 再定义一个全局变量
gl_name = "阿童木"


def demo():
    # 如果局部变量名字和全局变量的名字相同
    # pycharm会在局部变量下方显示一个灰色的虚线
    num = 99

    print("%d"%num)
    print("%s" % gl_title)
    print("%s" % gl_name)

demo()

