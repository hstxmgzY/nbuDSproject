# 导入聚宽函数库
import jqdata

# 全局变量
'''
g = {

    'total_days': 0,  # 总回测天数
    'days': 0,  # 当前回测天数
    'start_date': "2010-01-01",  # 回测开始日期
    'end_date': "2021-01-01",  # 回测结束日期
    'indicator_list': ["指标1", "指标2", "指标3", "指标4", "指标5", "指标6", "指标7", "指标8", "指标9"],
    'previous_signal': 0  # 前一次交易信号
}
'''
# 全局变量
g = {
     'stock':['股票1','股票2','股票3'],
    'total_days': 0,  # 总回测天数
    'days': 0,  # 当前回测天数
    'start_date': "2010-01-01",  # 回测开始日期
    'end_date': "2021-01-01",  # 回测结束日期
    'indicator_list': ["CCI(5)", "EMA(5)", "AD", "RSI(5)", "WilliamsR(5)", "MACD(5, 15)", "MA(5)", "OBV(5)",
                       "ADOSC(5)"],
    'previous_signal': 0  # 前一次交易信号
}



#交易信号存储变量：
#signal_history=[0 for  i in range(g['end_date']-g['start_date'])]
signal_history=[[0 for j in range(3650)] for i in range(len(g['indicator_list']))]
#缺乏精准的日期计算，临时申请十年3650天
open_history=[[0 for n in range(3650)] for m in range(len(g['stock']))]
close_history=[[0 for p in range(3650)] for o in range(len(g['stock']))]
volume_history=[[0 for z in range(3650)] for x in range(len(g['stock']))]
high_history=[[0 for v in range(3650)] for b in range(len(g['stock']))]
low_history=[[0 for a in range(3650)] for s in range(len(g['stock']))]



def history(p,unkownstring,indicator):

    indicator_id=g['indicator_list'].index(indicator)
    pdays_signal=[]
    for i in range(p):
        pdays_signal.append(signal_history[indicator_id][g['days']-i])

    return pdays_signal

'''
# 计算交易信号
def calculate_trading_signal(context):
    # 获取前一次交易信号
    prev_signal = g['previous_signal']

    # 计算当日的交易信号
    buy_votes = 0
    sell_votes = 0

    # 遍历指标列表
    for indicator in g['indicator_list']:
        # 获取指标规则在前三天内的交易信号
        signals = history(3, "1d", indicator)
        if signals[-1] == "买入":
            buy_votes += 1
        elif signals[-1] == "卖出":
            sell_votes += 1

    # 判断是否需要逆转交易信号
    if prev_signal == "买入" and sell_votes > buy_votes:
        signal = "卖出"
    elif prev_signal == "卖出" and buy_votes > sell_votes:
        signal = "买入"
    else:
        signal = prev_signal

    # 更新当前交易信号
    context.current_signal = signal

    # 更新前一次交易信号
    g['previous_signal'] = signal
'''

# 主要的交易逻辑函数，每个交易日调用
def handle_data(context, bar_dict):
    # 更新回测天数
    g['days'] += 1

    # 每个交易日计算交易信号
    calculate_trading_signal(context)

    # 输出交易信号
    print("当前交易信号:", context.current_signal)

    # 判断是否到达回测结束日期
    if g['days'] >= g['total_days']:
        # 结束回测
        return


# 运行回测函数
jqdata.run_backtest(strategy_id="my_strategy",
                    initialize=initialize,
                    handle_data=handle_data,
                    start_date=g['start_date'],
                    end_date=g['end_date'],
                    frequency='daily',
                    account_type='stock',
                    # 其他参数设置
                    )

# 初始化函数，在回测前调用
def initialize(context):
    pass




# 计算交易信号
def calculate_trading_signal(context):
    # 获取前一次交易信号
    prev_signal = g['previous_signal']

    # 计算当日的交易信号
    buy_votes = 0
    sell_votes = 0

    # 遍历指标列表
    for indicator in g['indicator_list']:
        # 获取指标规则在前三天内的交易信号
        signals = history(3, "1d", indicator)

        # 根据不同指标的交易信号判断增加买入票数或卖出票数
        if indicator.startswith("CCI"):
            if signals[-2] < 60 and signals[-1] > 60:
                buy_votes += 1
            elif signals[-2] > -60 and signals[-1] < -60:
                sell_votes += 1
        elif indicator.startswith("EMA"):
            if signals[-2] < signals[-1]:
                buy_votes += 1
            elif signals[-2] > signals[-1]:
                sell_votes += 1
        elif indicator == "AD":
            if signals[-2] < signals[-1]:
                buy_votes += 1
            elif signals[-2] > signals[-1]:
                sell_votes += 1
        elif indicator.startswith("RSI"):
            if signals[-2] > 30 and signals[-1] < 30:
                buy_votes += 1
            elif signals[-2] < 70 and signals[-1] > 70:
                sell_votes += 1
        elif indicator.startswith("WilliamsR"):
            if signals[-2] < -60 and signals[-1] > -60:
                buy_votes += 1
            elif signals[-2] > -40 and signals[-1] < -40:
                sell_votes += 1
        elif indicator.startswith("MACD"):
            if signals[-2] > signals[-3] and signals[-1] < signals[-2]:
                buy_votes += 1
            elif signals[-2] < signals[-3] and signals[-1] > signals[-2]:
                sell_votes += 1
        elif indicator.startswith("MA"):
            if signals[-2] > signals[-1]:
                buy_votes += 1
            elif signals[-2] < signals[-1]:
                sell_votes += 1
        elif indicator.startswith("OBV"):
            if signals[-2] < signals[-1] and close[-2] < close[-1]:
                buy_votes += 1
            elif signals[-2] > signals[-1] and close[-2] > close[-1]:
                sell_votes += 1
        elif indicator.startswith("ADOSC"):
            if signals[-2] < 0 and signals[-1] > 0:
                buy_votes += 1
            elif signals[-2] > 0 and signals[-1] < 0:
                sell_votes += 1

    # 判断是否需要逆转交易信号
    if prev_signal == "买入" and sell_votes > buy_votes:
        signal = "卖出"
    elif prev_signal == "卖出" and buy_votes > sell_votes:
        signal = "买入"
    else:
        signal = prev_signal

    # 更新当前交易信号
    context.current_signal = signal

    # 更新前一次交易信号
    g['previous_signal'] = signal







# 主要的交易逻辑函数，每个交易日调用
def handle_data(context, bar_dict):
    # 更新回测天数
    g['days'] += 1

    # 每个交易日计算交易信号
    calculate_trading_signal(context)

    # 输出交易信号
    print("当前交易信号:", context.current_signal)

    # 判断是否到达回测结束日期
    if g['days'] >= g['total_days']:
        # 结束回测
        return


# 运行回测函数
jqdata.run_backtest(strategy_id="my_strategy",
                    initialize=initialize,
                    handle_data=handle_data,
                    start_date=g['start_date'],
                    end_date=g['end_date'],
                    frequency='daily',
                    account_type='stock',
                    # 其他参数设置
                    )



import talib

# 假设你已经获取了相应的价格数据，例如收盘价(close)和最高价(high)，以及成交量(volume)等


stock=''#例子

def attribute_history(stock,days,unkownstr,feature):
    h={
        'high':[],
        'low':[],
        'volume':[],
        'close':[]
    }
    stock_id=g['stock'].index(stock)
    for i in range(days):
        h['high'].append(high_history[stock_id][g['days']-i])
        h['low'].append(low_history[stock_id][g['days']-i])
        h['volume'].append(volume_history[stock_id][g['days']-i])
        h['close'].append(close_history[stock_id][g['days']-i])
    return h




h = attribute_history(stock, 15, '1d', ('open', 'close', 'volume', 'factor'))
high = h['high'][-1]
low = h['low'][-1]
volume = h['volume'][-1]
close=h['close'][-1]

# 计算CCI指标
cci = talib.CCI(high, low, close, timeperiod=5);

# 计算EMA指标
ema = talib.EMA(close, timeperiod=5);

# 计算AD指标
ad = talib.AD(high, low, close, volume);

# 计算RSI指标
rsi = talib.RSI(close, timeperiod=5);

# 计算Williams %R指标
williams_r = talib.WILLR(high, low, close, timeperiod=5);

# 计算MACD指标
macd, macd_signal, _ = talib.MACD(close, fastperiod=5, slowperiod=15, signalperiod=9);

# 计算移动平均指标
ma = talib.MA(close, timeperiod=5);

# 计算OBV指标
obv = talib.OBV(close, volume);

# 计算ADOSC指标
adosc = talib.ADOSC(high, low, close, volume, fastperiod=3, slowperiod=10);

# 打印指标数值
print("CCI:", cci);
print("EMA:", ema);
print("AD:", ad);
print("RSI:", rsi);
print("Williams %R:", williams_r);
print("MACD:", macd);
print("MACD Signal:", macd_signal);
print("MA:", ma);
print("OBV:", obv);
print("ADOSC:", adosc);
'''
•last_price: 最新价
•high_limit: 涨停价
•low_limit: 跌停价
•paused: 是否停止或者暂停了交易, 当停牌、未上市或者退市后返回
True
•is_st: 是否是
ST(包括ST, *ST)，是则返回
True，否则返回
False
•day_open: 当天开盘价
'''




h = attribute_history(stock, 5, '1d', ('open', 'close', 'volume', 'low'))  # 取得000001(平安银行)过去5天的每天的开盘价, 收盘价, 交易量, 复权因子
# 不管df等于True还是False, 下列用法都是可以的
open_price=h['open'][-1] ; # 过去5天的每天的开盘价, 一个pd.Series对象, index是datatime
close_price=h['close'][-1];  # 昨天的收盘价
#h['open'].mean();
h = attribute_history(stock,5, '1d', ('open', 'close', 'volume', 'factor'));
high = h['high'][-1];
low = h['low'][-1];
volume = h['volume'][-1];

