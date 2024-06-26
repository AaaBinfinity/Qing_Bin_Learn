"""
2024-6-26 09:58:51
"""
"""
列表的常用操作（方法）
列表除了可以：
·定义
·使用下标索引获取值
此外，列表也提供了一系列功能：
·插入元素
·删除元素
·清空列表
·修改元素
·统计元素个数
等等功能，这些功能我们都称之为：列表的方法
"""

"""
列表的查询功能（方法）
函数是一个封装的代码单元，可以提供特定功能
在Python中，如果将函数定义为class（类）的成员，那么函数会称之为：方法
"""

"""
    函数
def add(x,y):
    return x + y
    
    方法
class Student:

    def add(self,x,y):
        return x + y
"""
"""
方法和函数功能一样，有传入参数，有返回值，只是方法的使用格式不同：
函数的使用：num = add（1,2）
方法的使用：student = Student()
         num = student.add(1,2)
"""

"""
·查找某元素的下标
功能：查找指定元素在列表的下标，如果找不到，报错valueerror
语法：列表.index（元素）
index就是列表对象（变量）内置的方法（函数）
"""

# 演示数据容器之：list列表的常用操作
mylist = ['Bifinity', 'Qing', ]
# 1.1查找某元素在列表内的下标索引
index = mylist.index('Qing')
print(f"Qing在列表的下标索引值是：{index}")  # Qing在列表的下标索引值是：1
# 1·2如果被查找的元素不存在，会报错
# index = mylist.index('hello')
# print(f"hello在列表的下标索引值是：{index}")  # ValueError: 'hello' is not in list

"""
列表的修改功能（方法）
修改特定位置（索引）的元素值：
语法：列表[下标]=值
可以使用如上语法，直接对指定下标（正向、反向下标均可）的值进行：重新赋值（修改）
"""
# 2·修改特定下标索引的值
mylist[0] = "Bin"
print(mylist)  # ['Bin', 'Qing']

"""
插入元素：
语法：列表.insert（下标，元素），在指定的下标位置，插入指定的元素
"""
# 3·在指定下标位置插入新元素
mylist.insert(1, "loves")
print(mylist)  # ['Bin', 'loves', 'Qing']

"""
追加元素：
语法：列表.append(元素)，将指定元素，追加到列表的尾部
"""

# 4·在列表的尾部追加'''单个'''新元素
mylist.append("forever~")
print(mylist)  # ['Bin', 'loves', 'Qing', 'forever~']

"""
·追加元素方式2：
语法：列表.extend（其它数据容器），将其它数据容器的内容取出，依次追加到列表尾部
"""

# 5·在列表的尾部追加'''一批'''新元素
mylist2 = ['and', 'forever']
mylist.extend(mylist2)
print(mylist)  # ['Bin', 'loves', 'Qing', 'forever~', 'and', 'forever']

"""
删除元素：
语法1：del列表[下标]
语法2；列表.pop（下标）
"""

# 6.删除指定下标索引的元素（2种方式）
mylist = ['Bin', 'loves', 'Qing', 'forever~', 'and', 'forever']
# 6·1 方式1：del列表[下标]
del mylist[3]
print(f"列表删除元素后的结果是：{mylist}")  # 列表删除元素后的结果是：['Bin', 'loves', 'Qing', 'and', 'forever']
# 6·2 方式2：列表.pop（下标）
element = mylist.pop(3)
print(f"通过pop方法取出元素后列表内容：{mylist},取出的元素是：{element}")
# 通过pop方法取出元素后列表内容：['Bin', 'loves', 'Qing', 'forever'],取出的元素是：and

"""
删除某元素在列表中的第一个匹配项
语法：列表.remove（元素）
"""

# 7·删除某元素在列表中的第一个匹配项
mylist = ['Bin', 'loves', 'Qing', 'forever', 'and', 'forever']
mylist.remove("forever")
print(f"通过remove方法移除元素后，列表的结果是：{mylist}")

"""
清空列表内容
语法：列表.clear（）
"""

# 8·清空列表
mylist.clear()
print(f"列表被清空了，结果是：{mylist}")  # []

"""
统计某元素在列表内的数量
语法：列表.count(元素)
"""

# 9·统计某元素在列表内的数量
mylist = ['Bin', 'loves', 'Qing', 'forever', 'and', 'forever']
mylist.count("forever")
count = mylist.count("forever")
print(f"列表中forever的数量是{count}")  # 列表中forever的数量是2

"""
·统计列表中有多少元素
语法：len（列表）
可以得到一个int数字，表示列表内的元素数量
"""
# 统计列表中全部的元素数量
mylist = ['Bin', 'loves', 'Qing', 'forever', 'and', 'forever']
count = len(mylist)
print(f"列表的元素数量，总共有：{count}个")  # 列表的元素数量，总共有：6个

"""
列表的特点：
·可以容纳多个元素（上限为2**63-1）
·可以容纳不同类型的元素（混装）
·数据是有序存储的（有下标序号）
·允许重复数据存在
·可以修改（增加或删除元素等）
"""

# 练习案例

"""
2024年6月26日16:33:48
"""
