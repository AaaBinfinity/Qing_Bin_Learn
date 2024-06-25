"""
2024年6月25日14:48:20
"""

"""
列表的定义：
基本语法：

# 字面量
[元素1，元素2，元素3，元素4.....]

# 定义变量
变量名称 = [元素1，元素2，元素3，元素4...]

# 定义空列表
变量名称 = []
变量名称 = list[]

列表内的每一个数据，称之为元素
·以[]
列表内的每一个元素之间用，逗号隔开
"""
# 使用[]的方式定义列表
name_list = ["曹老板", "卿卿"]  # ['曹老板', '卿卿']
print(name_list)
print(type(name_list))  # <class 'list'>

# 可以是不同类型
my_list = ["binfinity", '0328']
print(my_list)  # ['binfinity', '0328']
print(type(my_list))  # <class 'list'>

# 嵌套列表的定义
you_list = [[0, 5, 0, 1, 0, 2], [3, 28]]
print(you_list)  # [[0, 5, 0, 1, 0, 2], [3, 28]]
print(type(you_list))  # <class 'list'>

"""
注意：列表可以一次存储多个数据，且可以为不同的数据类型，支持嵌套
"""
