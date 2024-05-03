"""
案例需求：
 定义一个数字（1~10随机产生），通过3次判断来猜出数字

案例要求：
1.数字随机产生，范围1~10
2.有3次机会猜数字，通过3层嵌套判断实现
3.每次猜不中，会提示大了或小了
"""

print("Hi Player~")

import random

num = random.randint(1, 10)
print("让我们一起猜数字吧~")
guess1 = int(input("你猜的数字是:"))
if guess1 != num:
    if guess1 > num:
        print("太大啦，再试一次吧~")
    elif guess1 < num:
        print("太小啦，再试一次吧~")

    guess2 = int(input("你猜的数字是~"))
    if guess2 != num:
        if guess2 > num:
            print("太大啦，再再试一次吧~")
        elif guess2 < num:
            print("太小啦，再再试一次吧~")

        guess3 = int(input("你猜的数字是~"))
        if guess3 != num:
            if guess3 > num:
                print("太大啦，别试了笨蛋~")
            elif guess3 < num:
                print("太小啦，别试了笨蛋~")

        else:
            print("猜对啦，棒棒哒~")
    else:
        print("猜对啦，棒棒哒~")
else:
    print("对了捏宝宝~")
