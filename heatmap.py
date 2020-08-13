import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
def heatmap(datatable):
    '''
    相关系数热力图
    '''
    correlation = datatable.corr()
    sns.heatmap(correlation, annot=True)
    plt.show()