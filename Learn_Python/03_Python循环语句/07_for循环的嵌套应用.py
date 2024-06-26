"""
2024年5月30日20:06:26
"""

"""
程序中的嵌套for循环：
for 临时变量 in 待处理数据集（序列）：
    循环满足条件应做的事情1
    循环满足条件应做的事情2
    循环满足条件应做的事情N
    ...
    for 临时变量 in 待处理数据集（序列）：
        循环满足条件应做的事情1
        循环满足条件应做的事情2
        循环满足条件应做的事情N
"""

"""
以向小美表白为例
·坚持表白100天
·每天送花10朵
"""
#
# i = 1
# for i in range(1, 100):
#     print(f"今天是向小美表白的第{i}天~")
#     for j in range(1, 11):
#         print(f"送给小美第{j}朵玫瑰花")
#
# print(f"第{i}天，表白成功！")

"""
可以外部是for循环，内部是while循环
也可以外部是while循环，内部是for循环
"""

# 练习案例，for循环打印九九乘法表
i = 1
for j in range(1, 10):
    while i <= j:
        print()
        print(f"{i}*{j} = {i * j}", end='')
        i += 1
        j += 1


