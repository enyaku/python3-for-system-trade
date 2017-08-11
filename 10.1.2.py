

import pandas as pd
import numpy as np
sigma=0.1/np.sqrt(250)
print(sigma)
P=[1]
for i in range(1,250):
    w=np.random.normal(0,1)
    P.append(P[i-1]+sigma*w)


price=pd.Series(P)
dp=price.diff().dropna()
print("mean %2.5f std %2.5f skew %2.5f kurt %2.5f"\
%(dp.mean(),dp.std(),dp.skew(),dp.kurt()))


import matplotlib.pyplot as plt
plt.figure(figsize=(8,3.2))
plt.subplot(121)
price.plot(color='darkgray')
plt.xlabel('t')
plt.ylabel('$P_t$')
plt.subplot(122)
dp.hist(color='lightgreen')
mx=round(dp.max(),2)
mn=round(dp.min(),2)
plt.xticks([mn,0,mx])
plt.xlabel('$P_t-P_{t-1}$')
plt.ylabel('frequency')

P=[]
dP=[]
high=[0]*250
low=[1]*250
for j in range(10000):
    P0=1
    for i in range(250): 
        w=np.random.normal(0,1)
        dp=sigma*w
        P0=P0+dp
        if P0>high[i]:
            high[i]=P0
        if P0<low[i]:
            low[i]=P0
        dP.append(dp)
    P.append(P0)
price=pd.Series(P)
dprice=pd.Series(dP)


plt.figure(figsize=(9,4))
plt.subplot(1,2,1)
plt.plot(high,label="high",linestyle='--')
plt.plot(low,label="low",color='darkgray')
plt.title('max$P_t$-min$P_t$')
plt.xlabel('t')
plt.ylabel('$P_t$')
plt.legend(loc='upper left')
plt.subplot(1,2,2)
price.hist(bins=100,color='lightyellow')
plt.xlabel('$P_{250}$')
plt.ylabel('frequency')
print("mean %2.5f std %2.5f skew %2.5f kurt %2.5f"\
%(dprice.mean(),dprice.std(),dprice.skew(),dprice.kurt()))





plt.show()

