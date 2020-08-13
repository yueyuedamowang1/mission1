import pandas as pd
import akshare as ak
from matplotlib import pyplot as plt
import seaborn as sns
a=ak.stock_zh_a_daily(symbol='sh600418')
a=a.dropna()
a=a.reset_index()
raw_time = pd.to_datetime(a.pop('date'), format='%Y/%m/%d %H:%M')
print (raw_time)
print(a)
plt.plot(raw_time, a['close'])
plt.xlabel('Time')
plt.ylabel('Share Price')
plt.title('Trend')
plt.show()