def scatter_plot():
    s=input("输入散点图所取的点数，最好大于400:")
    point =int (s)
    plt.scatter(a['volume'][:point], a['close'][:point])
    plt.xlabel('Volume')
    plt.ylabel('Share Price')
    plt.title('Volume & Share Price')
    return plt.show()


a = statisticsGet("sh600418")
def scatter_plot(): 
    plt.scatter(a['volume'], a['close'])
    plt.xlabel('Volume')
    plt.ylabel('Share Price')
    plt.title('Volume & Share Price')
    
    return plt.show()
    
scatter_plot()
