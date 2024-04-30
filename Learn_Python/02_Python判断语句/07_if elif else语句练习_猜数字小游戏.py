# # # 卿卿亲笔

# 猜数游戏
# 定义一个我想到的数字
num = 5
# 用户输入一个数字
# 判断
# 第一次判断，如果正确，棒棒
if int(input("猜猜我想到的数字~")) == num:
    print("太酷啦")
# 如果错误，再试一次
elif int(input("再试一次~")) == num:
    print("宝宝太棒啦~")
# 如果再错误，再试最后一次
elif int(input("再试最后一次3~")) == num:
    print("聪明宝宝真棒呀！")
# 如果全部猜错，那么sorry啦~
elif int(input("再试最后最后一次2~")) == num:
    print("√")
else:
    print(f"sorry啦~我想的数字是{num}")



# 史山代码

num = 1
if int(input()) != num:
    print("again1")
    if int(input()) != num:
        print("again2")
        if int(input()) != num:
            print(f"is{num}")
        else:
            print("yes")
    else:
        print("yes")
else:
    print("yes")
