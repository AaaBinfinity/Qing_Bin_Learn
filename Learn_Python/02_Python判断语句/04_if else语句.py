"""

生活中的判断：

    如果——————————→动作1
    否则——————————→动作2


if语句 满足条件会执行代码，不满足不会执行
在Python中，可以通过 if else 的组合使用来实现 if 不满足条件时仍可以执行代码

程序中的判断：
    语法：
        if 条件:
            满足条件要做的行为1
            满足条件要做的行为2
            满足条件要做的行为3
            满足条件要做的行为4
                ......
        else:
            不满足条件要做的行为1
            不满足条件要做的行为2
            不满足条件要做的行为3
            不满足条件要做的行为4
                 ......

else后面不需要判断条件，但实行语句仍需要缩进

"""

# 欢迎程序
print("欢迎来到游乐城")
# 通过用户输入获取用户年龄
age = int(input("请输入您的年龄："))
# 判断是否成年
if age >= 18:
    print("您已成年，请购买成人票")  # 条件成立时执行
else:       # 注意缩进，else应该是和 if 同级的
    print("您未成年，请购买儿童票")  # 条件不成立时执行
# 祝福程序
print("Have A Good Time!")
