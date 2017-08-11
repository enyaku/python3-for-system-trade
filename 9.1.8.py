from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import pandas_datareader.data as web
import numpy as np
import matplotlib.pyplot as plt


plt.figure(figsize=(6,3))
ax=plt.subplot(1,1,1)

n225 = web.DataReader("NIKKEI225", 'fred',"1949/5/16").dropna()
rn225=n225.pct_change().dropna()


import statsmodels.api as sm
fig = plt.figure(figsize=(8,4))
ax1=fig.add_subplot(1,2,1)
plt.scatter(rn225,rn225.shift(1),color='gray',alpha=0.05)
plt.xticks([-0.2,0,0.2])
plt.title('1 days')
plt.xlabel('$P_{t-1}/P_{t-2}-1$')
plt.ylabel('$P_{t}/P_{t-1}-1$')
plt.hlines([0],-0.1,0.1)
plt.vlines([0],-0.1,0.1)
ax2=fig.add_subplot(1,2,2)
fig=sm.graphics.tsa.plot_acf(rn225.squeeze(), lags=5,ax=ax2,color='gray')






plt.show()

