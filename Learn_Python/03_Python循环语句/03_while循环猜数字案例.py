"""
设置一个范围1~100的随机整数变量，通过while循环，配合input语句，判断输入的数字是否等于随机数
1.无限次机会，直到猜中为止
2.每次猜不中，会提示大了或者小了
3.猜完数字后，提示猜了几次
"""

# 合作共赢版

count = 0
# 随机数字
import random

num = random.randint(1, 10)
flag = True
# 无限次机会
while flag:
    count += 1
    num_guess = int(input("请猜测一个数字"))
    if num_guess == num:
        print("你真棒")
        print(f"你一共输入了{count}次")
        flag = False
    elif num_guess > num:
        print("大了捏")
    elif num_guess < num:
        print("小了捏")
# 2024.05.06
