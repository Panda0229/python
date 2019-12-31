from zhn_01_测试模块1 import say_hello as module2_say_hallo
from zhn_02_测试模块2 import say_hello

module2_say_hallo()
say_hello()


# 如果 两个模块，存在 同名的函数，那么 后导入模块的函数，会 覆盖掉先导入的函数
# 开发时 import 代码应该统一写在 代码的顶部，更容易及时发现冲突
# 一旦发现冲突，可以使用 as 关键字 给其中一个工具起一个别名

