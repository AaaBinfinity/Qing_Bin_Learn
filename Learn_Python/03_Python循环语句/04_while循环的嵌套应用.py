# 2024年5月7日19:39:37
"""
while 条件1：
    条件1满足时，做的事情1
    条件1满足时，做的事情2
    条件1满足时，做的事情3
    ...（省略）...

    while 条件2：
        条件2满足时，做的事情1
        条件2满足时，做的事情2
        条件2满足时，做的事情3
        ...(省略)...
"""

# 卿卿亲笔
# 外层：表白100天的控制
i = 1
while i <= 100:
    print(f"今天是第{i}天，准备表白...")
    # 内层：每天的表白都送18只玫瑰花
    j = 1
    while j <= 10:
        print(f"送给小美第{j}只玫瑰花")
        j = j + 1
    print("小美我喜欢你")
    i += 1

print(f"坚持到第{i-1}天，表白成功")
