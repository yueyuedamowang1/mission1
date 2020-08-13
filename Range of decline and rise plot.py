a = statisticsGet("sh600418")
def Range_of_decline_and_rise_plot():
    s=input("输入跌涨图步长，不要超过400的数：")
    step=int(s)
    spot_number = int(4000 / step)
    raw_time =timeGet(a) #a是股票中提取的数据
    daily_return = a['close'][0::step].pct_change().dropna()
    plt.plot(raw_time[step::step][:spot_number], daily_return[:spot_number])
    plt.xlabel('Time')
    plt.ylabel('Rise and Fall')
    plt.title('Range of decline and rise')
    return  plt.show()

Range_of_decline_and_rise_plot()
