"""
2024年6月25日08:42:08
"""

"""
所谓函数嵌套调用指的是一个函数里面又调用了另外一个函数
"""


# 定义函数func_b
def func_b():
    print("---2---")


# 定义函数func_a():,并在内部调用func_b
def func_a():
    print("---1---")

    #     嵌套调用函数func_b
    func_b()

    print("---3---")


# 调用函数fun_a
func_a()
