import pandas as pd
import akshare as ak
from matplotlib import pyplot as plt
import seaborn as sns
def statisticsGet(stockCode,stockRenewed=""):
    datatable=ak.stock_zh_a_daily(symbol=stockCode,adjust=stockRenewed)
    datatable=datatable.dropna()
    datatable=datatable.reset_index()
    return  datatable
def timeGet(DataTable):
    raw_time = pd.to_datetime(a.pop('date'), format='%Y/%m/%d %H:%M')
    return raw_time
 
a=statisticsGet('sh600418')
raw_time=timeGet(a)
plt.plot(raw_time, a['close'])
plt.xlabel('Time')
plt.ylabel('Share Price')
plt.title('Trend')
plt.show()