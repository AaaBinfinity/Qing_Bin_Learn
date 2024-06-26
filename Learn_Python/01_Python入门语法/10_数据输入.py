'''
input语句（函数）的使用

数据输出：print
数据输入：input
'''

# 使用input（）语句可以从键盘获取输入
# 使用一个变量接收（存储）input语句获取的键盘输入数据即可
print("请告诉我你是谁")  # 提示语句
name = input()
print("我知道了，你是%s" % name)

# 输出"请告诉我你是谁“的print语句其实是多余的
# 可以使用：input(提示信息)，在使用者输入内容前,显示提示内容
name = input("请告诉我你是谁")  # 提示信息可以直接写在input的括号里
print("我知道了，你是%s" % name)

# 无论写入的是什么样的数据，input语句通通都把它当做字符串来看待
num = input("李绮卿的学号是什么？")
print(f"id是：{num}")
print("李绮卿学号的类型是：", type(num))  # 接收到的是<class 'str'>

# 数据类型转换
num = input("李绮卿学号的类型是")
# 将接收到的字符串转化成整型
num = int(num)
print("李绮卿学号的类型是：", type(num))

print("I Love You")
# print("I Love You")
