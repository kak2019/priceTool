import tushare as ts

# 设置 Tushare 的 API token
ts.set_token('5be574099985a4a9564118e4812f7a2bab3ee9619ad8e3a23b025141')

# 初始化 pro 接口
pro = ts.pro_api()

# 获取海康威视的股价
df = pro.daily(ts_code='002415.SZ', start_date='20230801', end_date='20230819')

# 打印股价信息
print(df[['trade_date', 'close']])
