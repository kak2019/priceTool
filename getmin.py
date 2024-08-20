import time
import tushare as ts
import configparser
# 读取配置文件
config = configparser.ConfigParser()
config.read('config.ini')

# 从配置文件中获取 Tushare 的 API token
ts_token = config['tushare']['api_token']
ts.set_token(ts_token)


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
