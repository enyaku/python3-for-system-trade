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


fig=plt.figure(figsize=(6,3.1))
ax1=fig.add_subplot(1,2,1)
plt.scatter(r250n225,r250n225.shift(250),color='violet',alpha=0.05)
plt.title('250 days')
plt.xlabel('$P_{t-250}/P_{t-500}-1$')
plt.ylabel('$P_{t}/P_{t-250}-1$')
plt.hlines([0],-0.8,1.8)
plt.vlines([0],-0.8,2)
ax2=fig.add_subplot(1,2,2)
fig=sm.graphics.tsa.plot_acf(r250n225.squeeze(),lags=500,ax=ax2,color='gray')






plt.show()

