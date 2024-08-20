import time
import tushare as ts

# 设置 Tushare 的 API token
ts.set_token('5be574099985a4a9564118e4812f7a2bab3ee9619ad8e3a23b025141')

while True:
    # 获取实时行情数据
    df = ts.get_realtime_quotes('002415')
    df1 = ts.get_realtime_quotes('603369')

    # 将需要输出的内容拼接成一行
    output = f"{df['code'].iloc[0]} {df['name'].iloc[0]} {df['price'].iloc[0]} {df['time'].iloc[0]} | " \
             f"{df1['code'].iloc[0]} {df1['name'].iloc[0]} {df1['price'].iloc[0]} {df1['time'].iloc[0]}"

    print(output)

    # 每隔30秒刷新一次
    time.sleep(30)
