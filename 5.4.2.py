

import pandas_datareader.data as web
import numpy as np

import matplotlib.pyplot as plt
import pandas_datareader.data as pdr


states=['recover','growth','stable','bubble','reform','now']
dates=["1949/5/16","1954/12/1",'1972/1/1',"1986/12/1","1993/11/1","2016/9/30"]
print(states)

print(dates)


struct_break=[('1949/5/16','recv'),('1954/12/1','  growth'),
              ('1972/1/1','stable'),('1986/12/1','bubble'),('1991/3/1','      reform')]



end='2016/9/30'
n225 = web.DataReader("NIKKEI225", 'fred',"1949/5/16",end).NIKKEI225








for i in range(len(dates)-1):
    vol=np.log(n225[dates[i]:dates[i+1]]).diff().std()
    print(states[i],': %2.4f ;'%vol,)










plt.figure(figsize=(8,4))
analysis= web.DataReader("aapl", 'google',"1990/1/1",end)
analysis['intraday']=0#None
analysis['overnight']=0#None
c0=analysis.Close.iloc[0]    
for i in range(1,len(analysis)):
    o=analysis.iloc[i,0]#列0
    c=analysis.iloc[i,3]#列3
    analysis.iloc[i,5]=c-o#列6　Intraday
    analysis.iloc[i,6]=o-c0#列７ overnight
    c0=c
analysis.Close.plot(label='Close',linewidth=1)
analysis.intraday.cumsum().plot(label="intraday",linestyle=":")
analysis.overnight.cumsum().plot(label="overnight",linestyle='--',linewidth=1)
plt.legend()
plt.ylabel('PL or aapl')
plt.legend(loc='lower left')




plt.show()

