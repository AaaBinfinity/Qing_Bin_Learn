"""
2024年6月25日08:53:30
"""
"""
变量作用域指的是变量的作用范围（变量在哪里可用，在哪里不可用）
主要分为两类：局部变量和全局变量
所谓局部变量是定义在函数体内部的变量，即只在函数体内部生效
"""


# eg.
def testA():
    num = 100
    print(num)


testA()  # 100
# print(num)  #报错：name'num' is not defined（出了函数体，局部变量就无法使用了）
# 变量a是定义在“testA”函数内部的变量，在函数外部访问则立即报错

"""
局部变量的作用：在函数体内部，临时保存数据，即当函数调用完成后，则销毁局部变量
"""

"""
所谓全局变量，指的是在函数体内、外都能生效的变量
"""

num = 200


# 演示全局变量
def test_a():
    print(f"test a: {num}")


def test_b():
    print(f"test b: {num}")


test_a()
test_b()
print(num)

"""
global关键字：
使用global关键字可以在函数内部声明变量为全局变量
"""

num = 100


def test_A():
    print(num)


def testB():
    # global关键字声明a是全局变量
    global num
    num = 200
    print(num)


testA()  # 结果：100
testB()  # 结果：200
