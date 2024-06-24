# 2024年6月24日15:46:22
"""
思考：如果函数没有使用return语句返回数据，那么函数有返回值吗？
实际上是有的

Python中有个特殊的字面量：None，其类型是：<class 'NoneType'>
无返回值的函数，实际上就是返回了：None这个字面量

None表示：空的，无实际意义的意思
函数返回的None，就表示，这个函数没有返回什么有意义的内容
也就是返回了空的意思
"""

"""
None类型的应用场景：
·用在函数无返回值上
·用在if判断上
    ·在if判断中，None等同于False
    ·一般用于在函数中主动返回None，配合if判断做相关处理
·用在声明无内容的变量上
    ·定义变量，但暂时不需要变量有具体值，可以用None来代替
#     暂不赋予变量具体值
    name = None
"""


# None用于if判断
def check_age(age):
    if age > 18:
        return "seccess"
    else:
        return None


result = check_age(16)
if not result:
    # 进入if表示result是None值，也就是False
    print("未成年，不可以进入网吧")

# None用于声明无初始内容的变量
name = None
