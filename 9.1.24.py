from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import pandas_datareader.data as web
import numpy as np
import matplotlib.pyplot as plt


plt.figure(figsize=(6,3))
ax=plt.subplot(1,1,1)

n225 = web.DataReader("NIKKEI225", 'fred',"1949/5/16").dropna()
rn225=n225.pct_change().dropna()
r250n225=n225.pct_change(250).dropna()


import statsmodels.api as sm

before=rn225.loc[:'1989/12/31']
after=rn225.loc['1989/12/31':]

before250=r250n225.loc[:'1989/12/31']
after250=r250n225.loc['1989/12/31':]



plt.figure(figsize=(5,2.8))
high=[0]*250;low=[0]*250;ave=[0]*250
for i in range(250):
    high[i]=float(n225.loc['1991/3/1':].pct_change(i).max())
    ave[i]=float(n225.loc['1991/3/1':].pct_change(i).mean())
    low[i]=float(n225.loc['1991/3/1':].pct_change(i).min())
plt.plot(high,label="high",linestyle=':')
plt.plot(ave,label='ave')
plt.plot(low,label='low',linestyle='--')
plt.legend(loc='center right')
plt.title('after bubble crash')
plt.xlabel('$t$')
plt.ylabel('$P_{t}/P_{1}-1$')






plt.show()

