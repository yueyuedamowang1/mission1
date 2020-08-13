import pandas as pd
import akshare as ak
from matplotlib import pyplot as plt
import seaborn as sns
import  scatter_plot as sp
def statisticsGet(stockCode,stockRenewed=""):
    datatable=ak.stock_zh_a_daily(symbol=stockCode,adjust=stockRenewed)
    datatable=datatable.dropna()
    datatable=datatable.reset_index()
    return  datatable
def timeGet(DataTable,ListName='date'):
    raw_time = pd.to_datetime(DataTable.pop(ListName), format='%Y/%m/%d %H:%M')
   
    return raw_time
def plotTrend(DataTable,Raw_time,Listname='close'):
    plt.plot(Raw_time, DataTable[Listname])
    plt.xlabel('Time')
    plt.ylabel('Share Price')
    plt.title('Trend')
    plt.show()
a=statisticsGet('sh600418')
raw_time=timeGet(a)
 sp.scatter_plot()