"""
2024年5月31日15:54:25
"""

# continue
"""
continue关键字用于：中断本次循环，直接进入下一次循环
continue可以用于：for循环和while循环，效果一致
"""

for i in range(5):
    print("语句1")  # 在循环内，遇到continue就结束当次循环，进行下一次
    continue  # 所以，语句2不会执行
    print("语句2")  # 应用场景：
    # 在循环中，因某些原因，临时结束本次循环

# continue在嵌套循环中的应用
"""
continue关键字只可以控制：它所在的循环临时中断
"""
for i in range(5):
    print("语句1")
    for j in range(5):
        print("语句2")
        continue
        print("语句3")  # 不被执行
    print("语句4")

# break
"""
break关键字用于：直接结束循环
break可以用于：for循环和while循环，效果一致
"""

for i in range(5):
    print("语句1")
    break  # 在循环内，遇到break就结束循环了
    print("语句2")  # 所以，执行语句1后，直接执行语句3
print("语句3")

# break在嵌套循环中的应用
"""
break关键字只可以控制：它所在的循环结束
"""
for i in range(5):
    print("语句1")
    for j in range(5):
        print("语句2")  # 只输出1次，剩余4次不被执行
        break
        print("语句3")  # 不被执行
    print("语句4")
