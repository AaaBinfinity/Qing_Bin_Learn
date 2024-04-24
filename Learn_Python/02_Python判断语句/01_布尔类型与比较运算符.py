"""

判断广泛应用，例如，网站登录，密码核验，门禁刷卡等等

Python逻辑判断：

    如果（....）———（进行判断）———————————————————————→ 是 ————————→（执行“是”的代码）
                               ↓
                               ↓
                               ———————————————————→ 否 ————————→（执行“否”的代码）

"""

# 进行判断，只有两个结果：是，否
# 对应Python中的 True 和 False

'''
布尔类型（bool）：
    表示现实生活中的逻辑（真 和 假）
    * True      表示真     数字记为1
    * False     表示假     数字记为0
'''

# 定义变量用来储存布尔数据类型：变量名称 = 布尔类型字面量
Love = True
print(type(Love))  # <class 'bool'>

# 大于号就是一个比较运算符
result = 10 > 9  # 判断10和9哪个更大
print(f"10 > 9的结果是：{result}，result的类型为{type(result)}")  # 10 > 9的结果是：True，result的类型为<class 'bool'>

# "=="是一个比较运算符，判断左右是否相等
name_result = "QingQing" == "Binfinity"
print(
    "\"QingQing\"和\"Binfinity\"两个字符串是否相同的比较结果是"  # 这里的“+”(拼接字符串)可以省略
    f"{name_result}，类型是{type(name_result)}")  # False，类型是<class 'bool'>

"""

比较运算符

    运算符                                      描述                                             示例
    
     ==                         判断内容是否相等，满足为True，不满足为False                 a=3,b=3，则（a == b) 为 True

     !=                       判断内容是否不相等，满足为True，不满足为False                 a=1,b=3，则（a!=b）为True

      <                              判断运算符左侧内容是否小于右侧                         a=3,b=7，则（a < b）为True

      >                             判断运算符左侧内容是否大于右侧                          a=7,b=3，则（a> b）为True

     >=                             判断运算符左侧内容是否大于等于右侧                       a=3,b=3，则（a >= b）为True

      <=                            判断运算符左侧内容是否小于等于右侧                       a=3,b=3，则（a <= b) 为True

"""
