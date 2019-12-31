# 0到100所有偶数求和
i = 0
a = 0
while i <= 100:
    if i % 2 ==0:
    # 奇数判断 i % 2 ！=0
        print(i)
        a += i
    i += 1

print(a)

