import os


# 定义一个名为FlowerShop的类，用于模拟花店的管理和操作
class FlowerShop:
    # 初始化方法，创建一个FlowerShop对象时自动调用
    # 参数filename默认为'flowers.txt'，表示花店数据文件的名称
    def __init__(self, filename='flowers.txt'):
        self.filename = filename  # 设置文件名属性
        self.flowers = self.load_data()  # 加载花店数据，并存储在flowers属性中

    # 从文件中加载花店数据的方法
    def load_data(self):
        # 如果文件不存在，则返回空列表
        if not os.path.exists(self.filename):
            return []
        flowers = []  # 初始化一个空列表，用于存储加载的花数据
        # 以读模式打开文件，并逐行读取数据
        with open(self.filename, 'r') as f:
            for line in f:
                # 将每行数据按逗号分割，并转换为相应的数据类型，然后添加到flowers列表中
                name, price, quantity = line.strip().split(',')
                flowers.append({'name': name, 'price': float(price), 'quantity': int(quantity)})
        return flowers  # 返回加载的花数据列表

    # 将花店数据保存到文件的方法
    def save_data(self):
        # 以写模式打开文件，并将flowers列表中的数据逐行写入文件
        with open(self.filename, 'w') as f:
            for flower in self.flowers:
                f.write(f"{flower['name']},{flower['price']},{flower['quantity']}\n")

                # 添加新花的方法，需要花的名称、价格和数量作为参数

    def add_flower(self, name, price, quantity):
        # 遍历flowers列表，检查是否存在同名的花
        for flower in self.flowers:
            if flower['name'] == name:
                print(f"'{name}'已经有啦~")  # 如果存在，则打印提示信息并返回
                return
                # 如果不存在同名的花，则添加新的花到flowers列表中，并保存数据到文件
        self.flowers.append({'name': name, 'price': price, 'quantity': quantity})
        self.save_data()

        # 删除花的方法，需要花的名称作为参数

    def delete_flower(self, name):
        # 使用列表推导式创建一个新列表，其中不包含指定名称的花，然后更新flowers属性，并保存数据到文件
        self.flowers = [flower for flower in self.flowers if flower['name'] != name]
        self.save_data()

        # 更新花的信息的方法，需要花的名称、新价格（可选）和新数量（可选）作为参数

    def update_flower(self, name, price=None, quantity=None):
        # 遍历flowers列表，查找指定名称的花，并更新其价格和/或数量，然后保存数据到文件
        for flower in self.flowers:
            if flower['name'] == name:
                if price is not None:
                    flower['price'] = price
                if quantity is not None:
                    flower['quantity'] = quantity
                self.save_data()
                return
                # 如果没有找到指定名称的花，则打印提示信息
        print(f"'{name}' not found.")

        # 购买花的方法，需要花的名称和购买数量作为参数

    def purchase_flower(self, name, quantity):
        # 遍历flowers列表，查找指定名称的花，并检查库存是否足够，如果足够则扣减库存，并保存数据到文件
        for flower in self.flowers:
            if flower['name'] == name:
                if flower['quantity'] < quantity:
                    print(f"您所需的花朵 '{name}' 本店库存不足，已帮您反馈给老板啦.")  # 库存不足则打印提示信息并返回
                    return
                flower['quantity'] -= quantity  # 扣减库存
                self.save_data()  # 保存数据到文件
                print(f"您已成功购买{quantity}支'{name}'.")  # 打印购买信息
                return
                # 如果没有找到指定名称的花，则打印提示信息
        print(f"您需要的花朵 '{name}' 本店暂无哦，已反馈给老板~")

        # 查找花的方法，需要花的名称作为参数

    def search_flower(self, name):
        # 遍历flowers列表，查找指定名称的花，并打印其信息，如果没有找到则打印提示信息
        for flower in self.flowers:
            if flower['name'] == name:
                print(f"Flower: {flower['name']}, Price: {flower['price']}, Quantity: {flower['quantity']}")
                return
        print(f"Flower '{name}' not found.")

        # 显示所有花的信息的方法，无需参数

    def display_flowers(self):
        # 遍历flowers列表，并打印每朵花的信息
        for flower in self.flowers:
            print(f"花朵: {flower['name']}, 单价: {flower['price']}, 现有库存: {flower['quantity']}")


# 创建一个Shop实例
shop = FlowerShop()


def show_menu():
    print("""  
请选择操作：  
1. 消费者登录 
2. 管理员登录  
3. 退出程序  
    """)


def consumer_functions():
    print("消费者已登录。")
    flower_name = 'Rose'
    shop.search_flower(flower_name)  # 搜索某种鲜花的信息
    # 其他消费者功能可以在这里添加


def admin_functions():
    print("管理员可使用的功能：")
    print("1. 显示所有鲜花")
    print("2. 添加鲜花")
    print("3. 购买鲜花")
    print("4. 更新鲜花信息")
    print("5. 删除鲜花")
    choice = input("请选择要执行的操作：")
    if choice == '1':
        shop.display_flowers()
        print("操作完成")
    elif choice == '2':
        shop.add_flower('Rose', 5.99, 100)
        print("操作完成")
    elif choice == '3':
        shop.purchase_flower('Rose', 10)
        print("操作完成")
    elif choice == '4':
        shop.update_flower('Rose', price=6.99, quantity=50)
        print("操作完成")
    elif choice == '5':
        shop.delete_flower('Rose')
        print("操作完成")
    else:
        print("无效的选择，请重新选择。")

    # 主程序循环


while True:
    show_menu()
    choice = input("请输入您的选择（输入序号即可）：")
    if choice == '1':
        consumer_functions()
    elif choice == '2':
        password = input("请输入管理员密码：")
        if password == "050328":
            print("管理员已登录。")
            admin_functions()
        else:
            print("密码错误，请重试或选择其他功能。")
            break
    elif choice == '3':
        print("程序退出。")
        break
    else:
        print("无效选择，请重新输入。")
