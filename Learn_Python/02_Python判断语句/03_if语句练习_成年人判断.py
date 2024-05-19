# 欢迎程序
print("欢迎来到游乐城")
# 通过用户输入获取用户年龄
age = int(input("请输入您的年龄："))
# 判断是否成年
if age >= 18:
    print("您已成年，请购买成人票")
# 祝福程序
print("Have A Good Time!")

# 卿卿版
print("欢迎来到游乐场，儿童免费，成人收费")
age = int(input("请输入你的年龄"))
if age >= 18:
    print("您已成年，游玩需要补票10元")
print("祝您游玩愉快")


# 原始列表
original_list = [1, 9, 8, 7, 6, 5, 13, 3, 2, 1]

# 输出原列表
print("原列表:", original_list)

# 使用列表推导式创建一个只包含偶数的新列表
even_list = [x for x in original_list if x % 2 == 0]

# 输出新列表（只包含偶数）
print("删除奇数后的列表:", even_list)
