# 2024年5月9日18:35:14
# print输入不换行
"""
print("Hello")
print("World")

结果：
Hello
World
在print语句中，加上end=''即可输出不换行

print("Hello",end='')
print("World",end='')
结果：
HelloWorld
"""

"""
# 制表符\t
效果等同于tab键，可以让我们的多行字符串进行对齐
print("hello\tworld")
print("Qing\tBin")

结果：
hello world
Qing  Bin
"""

# 练习案例_打印九九乘法表
i = 1
while i <= 9:
    j = 1
    print()
    while j <= i:
        print(f"{j}*{i}={j*i}", end=" ")
        j += 1
    i = i + 1
