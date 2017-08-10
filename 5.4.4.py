

import pandas_datareader.data as web
import numpy as np

import matplotlib.pyplot as plt
import pandas_datareader.data as pdr

end='2016/9/30'



plt.figure(figsize=(8,4))



analysis= web.DataReader("DIA", 'google',"1993/1/29",end)
analysis['intraday']=0#None
analysis['overnight']=0#None
c0=analysis.Close.iloc[0]    
for i in range(1,len(analysis)):
    o=analysis.iloc[i,0]
    c=analysis.iloc[i,3]
    analysis.iloc[i,5]=c-o
    analysis.iloc[i,6]=o-c0
    c0=c
analysis.Close.plot(legend='Close')
analysis.intraday.cumsum().plot(legend="intraday",linestyle=':')
analysis.overnight.cumsum().plot(legend="overnight",linestyle='--')




plt.show()

