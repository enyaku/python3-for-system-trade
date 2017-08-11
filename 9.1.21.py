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


plt.figure(figsize=(8,4))
plt.subplot(121)
plt.scatter(before250,before250.shift(250),color='violet',alpha=0.05)
plt.xticks([-1,0,1])
plt.yticks([-1,0,2])
plt.hlines([0],-0.8,1.8)
plt.vlines([0],-0.8,2)
plt.title('bdfore')
plt.xlabel('$P_{t-250}/P_{t-500}-1$')
plt.ylabel('$P_{t}/P_{t-250}-1$')
plt.subplot(122)
plt.scatter(after250,after250.shift(250),color='seagreen',alpha=0.05)
plt.xticks([-1,0,1])
plt.yticks([-1,0,2])
plt.hlines([0],-0.8,1.8)
plt.vlines([0],-0.8,2)
plt.title('after')
plt.xlabel('$P_{t-250}/P_{t-500}-1$')
plt.ylabel('$P_{t}/P_{t-250}-1$')






plt.show()

