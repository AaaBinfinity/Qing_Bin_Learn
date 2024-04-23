# 公司名称
name = "星禾广告"
# 当前股价
stock_price = 19.99
# 股票代码
stock_code = "003032"
# 股票每日增长系数
stock_price_daily_growth_factor = 1.2
# 增长天数
growth_days = 7
# 最终股价
last_stock = stock_price * stock_price_daily_growth_factor** growth_days

# 计算，经过growth_days天的增长后，股价达到了多少钱
print(f"公司：{name},股票代码：{stock_code},当前股价：{stock_price}" )

print("每日增长系数是：%.1f,经过 %d 天的增长后，股价达到了：%.2f" % (stock_price_daily_growth_factor,growth_days,last_stock))