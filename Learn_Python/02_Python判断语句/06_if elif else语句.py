"""
if elif else 的组合使用可以实现某些场景下的多条件的判断
如果——————>动作
如果——————>动作
如果——————>动作
如果——————>动作、
实在不行————>动作


语法：
if 条件1:
     满足条件要做的行为1
     满足条件要做的行为2
     满足条件要做的行为3
     满足条件要做的行为4
elif 条件2:
     满足条件要做的行为1
     满足条件要做的行为2
     满足条件要做的行为3
     满足条件要做的行为4
elif 条件3:
     满足条件要做的行为1
     满足条件要做的行为2
     满足条件要做的行为3
     满足条件要做的行为4
else:
     条件都不满足时要做的行为1
     条件都不满足时要做的行为2
     条件都不满足时要做的行为3

"""

print("欢迎来到动物园")
height = int(input("请输入你的身高："))
vip_level = int(input("请输入你的vip等级（1~5）:"))
day = float(input("请输入今天日期："))
if height < 120:
    print("免费游玩")
elif vip_level > 3:
    print("免费游玩")
elif day == 11.11:
    print("ok玩吧~")
else:
    print("滚去交钱")
# print("代码执行完成")


# pro
print("欢迎来到动物园")

height = int(input("请输入你的身高："))

if height < 120:
    print("免费游玩")
else:
    vip_level = int(input("请输入你的vip等级（1~5）:"))
    if vip_level > 3:
        print("免费游玩")
    else:
        day = float(input("请输入今天日期："))
        if day == 11.11:
            print("欧克单身狗自己去玩叭~")
        else:
            print("呵呵")
