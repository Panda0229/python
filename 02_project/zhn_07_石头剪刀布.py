# 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
# 电脑 随机 出拳 —— 先假定电脑只会出石头，完成整体代码功能
# 比较胜负
#导入随即工具包
import random
haha = int(input("请出拳石头（1）／剪刀（2）／布（3）："))
print("haha选择是%d"%haha)
computer = random.randint(1,3)
print("haha%d - computer%d"%(haha,computer))
if ((haha == 1 and computer == 2)
        or (haha == 2 and computer == 3)
        or (haha == 3 and computer == 1)):
    print("你个垃圾")
elif haha == computer:
    print("接着整")
else:
    print("你个妹")

