bonuses = []
# 循环读取输入直到入职年限为-1
while True:
    years_of_service = int(input("请输入入职年限（输入-1结束）: "))
    if years_of_service == -1:
        break

    sales_amount = float(input("请输入销售业绩: "))

    if years_of_service > 5:
        if sales_amount > 15000:
            bonus_rate = 0.2
        elif sales_amount > 10000:
            bonus_rate = 0.15
        elif sales_amount > 5000:
            bonus_rate = 0.1
        else:
            bonus_rate = 0.05
    else:
        if sales_amount > 4000:
            bonus_rate = 0.045
        else:
            bonus_rate = 0.01

    bonus = sales_amount * bonus_rate
    bonuses.append(bonus)

print("奖金列表:", bonuses)