"""
2024年5月30日19:52:56
"""

for i in range(5):
    print(i)

print(i)  # 黄色警告框框

"""
for 临时变量 in 待处理数据集：
    循环满足条件时执行的代码
    
回看for循环语句的语法，会发现，将从数据集（序列）中取出的数据赋值给：临时变量
为什么是临时的呢？
临时变量，在编程规范上，作用范围（作用域），只限定在for循环内部

如果在for循环外部访问临时变量：
# 规范上：不允许
# 实际上：可以
"""

"""
如果真想在for循环外部访问临时变量：
"""

i = 0  # 提前把i定义出来
for i in range(5):
    print(i)

print(i)
