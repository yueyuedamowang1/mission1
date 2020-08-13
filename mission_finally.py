 
import misssion as ms
import heatmap as ht
import histogram as hg
import scatter_plot as sp
import range as rg
a=ms.statisticsGet('sh600418')
b=ms.timeGet(a)
ms.plotTrend(a,b)
ht.heatmap(a)
hg.histogram(a,1)
sp.scatter_plot(a,400)
rg.Range_of_decline_and_rise_plot(a,b)
