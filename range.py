import matplotlib.pyplot as plt
def Range_of_decline_and_rise_plot(a,b):
    daily_return = a['close'][::240].pct_change().dropna()
    plt.plot(b[240::240][:40],daily_return[:40])
    plt.xlabel('Time')
    plt.ylabel('Rise and Fall') 
    plt.title('Range of decline and rise')
    plt.show()

 
