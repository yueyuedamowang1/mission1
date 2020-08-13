import matplotlib.pyplot as plt
def scatter_plot(a,s=1):
    plt.scatter(a['volume'][:s], a['close'][:s])
    plt.xlabel('Volume')
    plt.ylabel('Share Price')
    plt.title('Volume & Share Price')
    plt.show()


 
 
 
