# 2024年5月19日16:53:56
"""
定义字符串变量name，内容为"QingQing loves Bin"
通过for循环，遍历此字符串，统计有多少个英文字母："i"
"""

name = 'QingQing loves Bin'
# 定义一个变量，用来统计有多少个i
count = 0  # 默认等于0，表示现在还没有统计到
for x in name:
    if x == "i":
        count += 1

print(f"被统计的字符串中有{count}个i")
