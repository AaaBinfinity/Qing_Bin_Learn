import json
import time  # 引入设计进度条的相关库

# 初始化
# 设置起始时间戳
start = time.perf_counter()
# 全局定义：
# 花卉信息总类"次数"：listtime = lt
lt = 3
# 花卉总数为：sum
sum = 0
# 循环介质置零：i
i = 0
# 内嵌默认账户（和管理员账户）
defaultuser = {'name': 'Binfinity', 'passwd': '050328'}

# 全局变量，用于存储花卉信息
flowers = []


def load_flowers(filename='flowers.txt'):
    """从文件中加载花卉信息"""
    global flowers
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                flowers.append({
                    'name': parts[0],
                    'price': float(parts[1]),
                    'stock': int(parts[2]),
                    'meaning': parts[3]
                })
    except FileNotFoundError:
        print("未找到仓库")


def save_flowers(filename='flowers.txt'):
    """将花卉信息保存到文件"""
    with open(filename, 'w', encoding='utf-8') as file:
        for flower in flowers:
            file.write(f"{flower['name']},{flower['price']},{flower['stock']},{flower['meaning']}\n")


def buy_flower():
    """购买花卉，并提供继续购买的选项"""

    # 在函数开始时加载花卉信息，而不是在每次购买前加载

    while True:  # 无限循环，直到用户选择不再购买
        name = input("请输入您想购买的花卉名称（或输入'退出'结束购买）：")
        if name.lower() == '退出':  # 提供退出的选项
            print("感谢您的购买，欢迎下次光临！")
            save_flowers()  # 在退出前保存最新的花卉信息
            break  # 退出循环

        quantity_str = input("请输入您想购买的数量：")

        # 尝试将输入的数量转换为整数
        try:
            quantity = int(quantity_str)
        except ValueError:
            print("购买数量必须是一个整数，请重新输入。")
            continue  # 跳过当前循环的剩余部分，重新开始循环

        flower_found = False
        for flower in flowers:
            if flower['name'] == name:
                flower_found = True
                if flower['stock'] >= quantity:
                    total_price = flower['price'] * quantity
                    flower['stock'] -= quantity
                    print(f"购买成功！您购买了{quantity}朵{name}，总价为{total_price}元。")
                    save_flowers()  # 购买成功后立即保存最新的花卉信息
                    break  # 找到并购买后退出循环
                else:
                    print(f"库存不足，无法购买{quantity}朵{name}。")

        if not flower_found:
            print(f"未找到花卉：{name}")

            # 询问用户是否继续购买
        continue_purchase = input("您是否想继续购买其他花卉？（是/否）：").strip().lower()
        if continue_purchase != '是':
            print("感谢您的购买，欢迎下次光临！")
            save_flowers()  # 在退出前保存最新的花卉信息
            break  # 如果用户不想继续购买，则退出循环


def view_stock():
    """查看库存"""
    for flower in flowers:
        print(f"花卉名称：{flower['name']}, 库存：{flower['stock']}")


def add_flower(name, price, stock, meaning):
    """添加花卉"""
    flowers.append({
        'name': name,
        'price': price,
        'stock': stock,
        'meaning': meaning
    })
    save_flowers()


def update_flower():
    """更新某个花卉信息，并在更新后进行比对确认"""
    global flowers
    flower_name = input("请输入要更新的花卉名称：")
    flower_found = False
    old_info = {}

    # 查找花卉并保存旧信息
    for flower in flowers:
        if flower['name'] == flower_name:
            flower_found = True
            old_info = flower.copy()  # 保存旧的花卉信息
            break

            # 如果没有找到花卉，则直接返回
    if not flower_found:
        print(f"未找到花卉：{flower_name}")
        return

        # 询问用户是否要更新价格、库存、花语
    new_price = None
    new_stock = None
    new_meaning = None

    if input("是否更新价格？(y/n) ").lower() == 'y':
        new_price = float(input("请输入新的价格："))

    if input("是否更新库存？(y/n) ").lower() == 'y':
        new_stock = int(input("请输入新的库存数量："))

    if input("是否更新花语？(y/n) ").lower() == 'y':
        new_meaning = input("请输入新的花语：")

        # 更新花卉信息
    for flower in flowers:
        if flower['name'] == flower_name:
            if new_price is not None:
                flower['price'] = new_price
            if new_stock is not None:
                flower['stock'] = new_stock
            if new_meaning is not None:
                flower['meaning'] = new_meaning
            break  # 找到并更新后退出循环

    # 保存更新后的花卉信息到文件（假设已实现save_flowers函数）
    save_flowers()

    # 显示更新前后的信息比对
    print(f"花卉信息已更新：{flower_name}")
    print("更新前信息：")
    print(f"名称：{old_info['name']}, 单价：{old_info['price']}, 库存：{old_info['stock']}, 花语：{old_info['meaning']}")
    # 获取更新后的花卉信息用于显示
    updated_flower = next((flower for flower in flowers if flower['name'] == flower_name), None)
    print("更新后信息：")
    print(
        f"名称：{updated_flower['name']}, 单价：{updated_flower['price']}, 库存：{updated_flower['stock']}, 花语：{updated_flower['meaning']}")


def delete_flower(name):
    """删除某个花卉"""
    for i, flower in enumerate(flowers):
        if flower['name'] == name:
            confirm = input(f"确认要删除{name}吗？(y/n): ")
            if confirm.lower() == 'y':
                del flowers[i]
                save_flowers()
                print(f"{name}已成功删除。")
                return
    print(f"未找到花卉：{name}")


def search_flower():
    """搜索某个花卉（通过花名或者花语），在函数体内请求用户输入关键词"""
    keyword = input("请输入要搜索的花卉名称或花语关键词：")
    results = []
    for flower in flowers:
        if keyword in flower['name'] or keyword in flower['meaning']:
            results.append(flower)
    if results:
        print(f"找到与关键词'{keyword}'匹配的花卉：")
        for flower in results:
            print(f"花卉名称：{flower['name']}, 花语：{flower['meaning']}")
    else:
        print(f"未找到与关键词'{keyword}'匹配的花卉。")

    # 调用函数，此时不需要传递参数


def view_all_products():
    """查看所有商品（花卉）的详细信息"""
    if flowers:
        print("所有花卉的详细信息如下：")
        for flower in flowers:
            print(f"花卉名称：{flower['name']}")
            print(f"花卉单价：{flower['price']} 元")
            # print(f"花卉库存：{flower['stock']}")
            print(f"花语：{flower['meaning']}")
            print("=" * 30)  # 分隔线，使信息更清晰

            print("=" * 30)  # 分隔线，使信息更清晰
    else:
        print("仓库中没有花卉信息。")
    print("全部花卉展示完毕！")


# 蜜汁进度条：
def Progress_bar():
    scale = 25
    print('加载中'.center(scale // 2, '-'))
    for i in range(scale + 1):
        a = '****' * i
        b = '....' * (scale - i)
        c = (i / scale) * 100
        dur = time.perf_counter() - start
        print('\r{:^3.0f}%[{}->{}]{:.2f}s'.format(c, a, b, dur), end='')
        time.sleep(0.1)
    print('\n' + '加载完成'.center(scale // 2, '-'))
    print("=" * 30)  # 分隔线，使信息更清晰


# 注册管理员
def Administrators_logup():
    print("=" * 30)  # 分隔线，使信息更清晰
    Administrators = []  # 使用列表来存储所有用户信息
    with open("Administrators.txt", 'r', encoding='utf-8') as f:
        for line in f:
            user_data = json.loads(line.strip())  # 使用json模块安全地解析数据
            Administrators.append(user_data)

    for i in range(4):
        name = input('请输入用户名：')
        passwd = input('请输入密码：')
        again_passwd = input('请再次输入密码：')

        if len(name.strip()) == 0:
            print('用户名不能为空，请重新输入。还可输入%d次' % (3 - i))
            continue

        if passwd != again_passwd:
            print('两次输入的密码不一致，请重新输入。还可输入%d次' % (3 - i))
            continue

        for user in Administrators:
            if name == user['name']:
                print('用户名重复，请重新输入。还可输入%d次' % (3 - i))
                break
        else:  # 如果没有找到重复的用户名，则执行以下代码块
            new_user = {'name': name, 'passwd': passwd}
            Administrators.append(new_user)
            with open("Administrators.txt", 'a', encoding='utf-8') as f:  # 以追加模式打开文件
                f.write(json.dumps(new_user) + '\n')  # 使用json模块安全地写入数据
            print('恭喜，注册成功')
            return  # 注册成功后直接退出函数，不再继续循环
    print('注册失败，已达到最大尝试次数')


# 管理员用户登录代码
def Administrators_login(shutdown):  # shutdown作为强制关闭词，用于输入次数过多强制退出
    print("=" * 30)  # 分隔线，使信息更清晰
    with open("Administrators.txt", 'r+', encoding='utf-8') as f:
        getinformation = f.readlines()  # 将文件的所有行读入到getinformation中
        tempAdministratorslist = []  # 创建一个临时列表用来存放所有的“字典”形式的字符串
        for count in range(3):  # 循环三遍，即三次输入错误的机会，三遍之后执行强制退出
            name = input('请输入用户名： ')
            password = input('请输入密码： ')
            for getit in getinformation:  # 把所有的字典循环一遍
                tempAdministratorslist.append(getit)  # 循环了导入到列表里
            for gettemplistline in tempAdministratorslist:  # 把列表循环一遍
                Administrators = eval(gettemplistline)  # 依次导入到Administrators中进行对比
                if (name != Administrators['name'] or password != Administrators['passwd']) and (
                        name != defaultuser['name'] or password != defaultuser['passwd']):
                    continue
                print('管理员登录成功！')
                shutdown = 1  # 强制关闭词，为0时触发
                return shutdown  # 将强制关闭词的值返回到主函数中去
            if (name == Administrators['name'] and password == Administrators['passwd']) and (
                    name != defaultuser['name'] or password != defaultuser['passwd']):
                continue
            lost = 2 - count  # lost用来计算剩余可试错次数
            if count < 2:
                print('用户名或密码错误,还有{:}次机会'.format(lost))
            else:
                alertexit = '输入错误次数过多，程序终止'
                print(alertexit)
                return 0

        f.close()


def logup():
    print("=" * 30)  # 分隔线，使信息更清晰
    users = []  # 使用列表来存储所有用户信息
    with open("users.txt", 'r', encoding='utf-8') as f:
        for line in f:
            user_data = json.loads(line.strip())  # 使用json模块安全地解析数据
            users.append(user_data)

    for i in range(4):
        name = input('请输入用户名：')
        passwd = input('请输入密码：')
        again_passwd = input('请再次输入密码：')

        if len(name.strip()) == 0:
            print('用户名不能为空，请重新输入。还可输入%d次' % (3 - i))
            continue

        if passwd != again_passwd:
            print('两次输入的密码不一致，请重新输入。还可输入%d次' % (3 - i))
            continue

        for user in users:
            if name == user['name']:
                print('用户名重复，请重新输入。还可输入%d次' % (3 - i))
                break
        else:  # 如果没有找到重复的用户名，则执行以下代码块
            new_user = {'name': name, 'passwd': passwd}
            users.append(new_user)
            with open("users.txt", 'a', encoding='utf-8') as f:  # 以追加模式打开文件
                f.write(json.dumps(new_user) + '\n')  # 使用json模块安全地写入数据
            print('恭喜，注册成功')
            return  # 注册成功后直接退出函数，不再继续循环
    print('注册失败，已达到最大尝试次数')


# 用户登录代码
def login(shutdown):  # shutdown作为强制关闭词，用于输入次数过多强制退出
    print("=" * 30)  # 分隔线，使信息更清晰
    with open("users.txt", 'r+', encoding='utf-8') as f:
        getinformation = f.readlines()  # 将文件的所有行读入到getinformation中
        tempuserslist = []  # 创建一个临时列表用来存放所有的“字典”形式的字符串
        for count in range(3):  # 循环三遍，即三次输入错误的机会，三遍之后执行强制退出
            name = input('请输入用户名： ')
            password = input('请输入密码： ')
            for getit in getinformation:  # 把所有的字典循环一遍
                tempuserslist.append(getit)  # 循环了导入到列表里
            for gettemplistline in tempuserslist:  # 把列表循环一遍
                users = eval(gettemplistline)  # 依次导入到users中进行对比
                if (name != users['name'] or password != users['passwd']) and (
                        name != defaultuser['name'] or password != defaultuser['passwd']):
                    continue
                print('登录成功！')
                shutdown = 1  # 强制关闭词，为0时触发
                return shutdown  # 将强制关闭词的值返回到主函数中去
            if (name == users['name'] and password == users['passwd']) and (
                    name != defaultuser['name'] or password != defaultuser['passwd']):
                continue
            lost = 2 - count  # lost用来计算剩余可试错次数
            if count < 2:
                print('用户名或密码错误,还有{:}次机会'.format(lost))
            else:
                alertexit = '输入错误次数过多，程序终止'
                print(alertexit)
                return 0

        f.close()


# 退出程序代码
def esc():
    alert = input('您确认要退出程序么？（输入"y"确认）：')
    if alert == 'y':
        print('系统退出')
        return 1


# 用户菜单
def Users():
    while True:
        print(
            """
    ！！！=========！！==！====！！=消费者登录=！！=====！====！！=====！！！
          1.显示所有花卉    2.购买花卉      3.搜索花卉     4.退出登录 
        """
        )
        # 消费者选择
        choose = input('请输入您选择的序号：')
        if choose == "1":
            print("▂﹍▂﹍▂﹍查看所有花卉▂﹍▂﹍▂﹍▂﹍▂  ")

            # 执行进度条
            Progress_bar()
            view_all_products()
            print("=" * 30)  # 分隔线，使信息更清晰
        elif choose == "2":
            print("▂﹍▂﹍▂﹍购买花卉▂﹍▂﹍▂﹍▂﹍▂")

            # 执行进度条
            Progress_bar()
            buy_flower()
            print("=" * 30)  # 分隔线，使信息更清晰
        elif choose == "3":
            print("▂﹍▂﹍▂﹍搜索花卉▂﹍▂﹍▂﹍▂﹍▂")

            # 执行进度条
            Progress_bar()
            search_flower()
            print("=" * 30)  # 分隔线，使信息更清晰
        elif choose == "4":
            print("=" * 30)  # 分隔线，使信息更清晰
            if esc() == 1:
                break

        else:
            print()
            print("﹏﹋﹏﹋﹏﹋﹏﹋﹏﹋﹏﹋﹏﹋﹏﹋﹏ ※”  ")
            print("选择无效，请输入正确的序号")


# 管理员菜单
def Administrators():
    while True:
        print(
            """
    ！！！=============！！=====！！=========！！=管理员登录=！！===========！！=====！！=======================！！！    
    
    1. 查看库存   2. 添加花卉   3. 购买花卉     4. 更新花卉信息    5. 删除花卉   6.添加管理员   7.搜索花卉    8.退出程序           
            """
        )
        # 用户选择2
        choose2 = input('请输入您选择的序号：')
        if choose2 == '1':
            print("▂﹍▂﹍▂﹍查看库存▂﹍▂﹍▂﹍▂﹍▂  ")

            # 执行进度条
            Progress_bar()
            view_stock()
        elif choose2 == '2':
            print("▂﹍▂﹍▂﹍添加花卉▂﹍▂﹍▂﹍▂﹍▂ ")

            # 执行进度条
            Progress_bar()
            print("！！！=============！！=====！！======")
            name = input("请输入您想添加的花卉名称")
            print("！！！=============！！=====！！======")
            price = input("请输入您想添加的花卉单价")
            print("！！！=============！！=====！！======")
            stock = input("请输入您想添加的花卉库存")
            print("！！！=============！！=====！！======")
            meaning = input("请输入您想添加的花卉花语")
            print("！！！=============！！=====！！======")
            add_flower(name=name, price=price, stock=stock, meaning=meaning)
            print("完成添加！！")
            print("！！！=============！！=====！！======")
        elif choose2 == '3':
            print("▂﹍▂﹍▂﹍购买花卉▂﹍▂﹍▂﹍▂﹍▂")
            # 执行进度条
            Progress_bar()
            buy_flower()
            print("！！！=============！！=====！！======")
        elif choose2 == '4':
            print("▂﹍▂﹍▂﹍更新花卉▂﹍▂﹍▂﹍▂﹍▂ ")
            # 执行进度条
            Progress_bar()
            update_flower()
        elif choose2 == '5':
            print("▂﹍▂﹍▂﹍删除花卉▂﹍▂﹍▂﹍▂﹍▂ ")

            # 执行进度条
            Progress_bar()
            delete_flower(name=input("请输入您想要删除的花卉："))
        elif choose2 == '6':
            print("▂﹍▂﹍▂﹍添加管理员▂﹍▂﹍▂﹍▂﹍▂")
            # 执行进度条
            Progress_bar()
            Administrators_logup()
        elif choose2 == "7":
            print("▂﹍▂﹍▂﹍搜索花卉▂﹍▂﹍▂﹍▂﹍▂ ")

            # 执行进度条
            Progress_bar()
            search_flower()
        elif choose2 == "8":
            esc()
            return 1
        else:
            print()
            print("﹏﹋﹏﹋﹏﹋﹏﹋﹏﹋﹏﹋﹏﹋﹏﹋﹏ ※”  ")
            print("选择无效，请输入正确的序号")


load_flowers()  # 加载花卉信息
# 执行进度条
Progress_bar()
print(
    """
    ★~☆·☆。~*∴*~★*∴ *·∴~*★*∴*★~☆·☆。~*∴*~★

    の┅∞   欢迎来到 Binfinity FlowerStore    の┅∞ 

    ★~☆·☆。~*∴*~★*∴ *·∴~*★*∴*★~☆·☆。~*∴*~★
    """
)
# 程序主循环：
while True:

    # 首页：
    print(
        """
" ……………·～·…οΟ○ の ○Οο…·～·…………… "

1.注册, 2.登录,3.管理员登录,4.退出程序
         """)
    # 用户选择1
    choosefirst = input('请输入您选择的序号：')
    if choosefirst == '1':
        print("▂﹍▂﹍▂﹍▂﹍▂﹍▂﹍▂﹍▂  ")

        logup()

        print(".*""*.*""*.*""*.*""**""*.*""**""*.*  ")

    elif choosefirst == '2':
        print("▂﹍▂﹍▂﹍▂﹍▂﹍▂﹍▂﹍▂  ")
        if login(1) == 0:
            break
        else:
            Users()
        print(".*""*.*""*.*""*.*""**""*.*""**""*.*  ")
    elif choosefirst == '3':
        if Administrators_login(1) == 0:
            break
        else:
            Administrators()

    elif choosefirst == '4':
        if esc() == 1:
            break
        else:
            print("程序继续运行")

    else:
        print("﹏﹋﹏﹋﹏﹋﹏﹋﹏﹋﹏﹋﹏﹋﹏﹋﹏ ※”  ")
        print("选择无效，请输入正确的序号")
