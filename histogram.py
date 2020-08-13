import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
def histogram(datatable,period):
    '''
    获得增长率的直方图
    '''
    daily_return = datatable['close'][0::period].pct_change().dropna()
    plt.hist(daily_return)
    plt.show()



