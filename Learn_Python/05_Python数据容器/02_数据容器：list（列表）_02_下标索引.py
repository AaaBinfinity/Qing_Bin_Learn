"""
2024年6月25日22:32:37
"""
"""
列表的下标（索引 ）
如何从列表中取出特定位置的数据？
我们可以使用：下标索引
[元素0 元素1 元素2 元素3 元素4 元素5]

列表的每个元素，都有其位置下标索引，从前向后的方向，从0开始，依次递增
只需要按照下标索引，即可取得对应位置的元素
"""

# 语法：列表[下标索引]
name_list = ['binfinity', 'QingQing']
print(name_list[0])  # binfinity
print(name_list[1])  # QingQing

'''
或者，可以反向索引，也就是从后向前：从-1开始，一次递减（-1、-2、-3....）
[元素-5 元素-4 元素-3 元素-2 元素-1]
'''
name_list = ['binfinity', 'QingQing']
print(name_list[-1])  # QingQing
print(name_list[-2])  # binfinity

# 嵌套列表的下标（索引）
"""
如果列表是嵌套的列表，同样支持下标索引
[[元素0，元素1]0，[元素0，元素1]1]
"""
my_list = [['binfinity', 'QingQing'], ['328', '512']]
print(my_list[1][1])  # 512
