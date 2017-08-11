

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




def ar1(beta,sigma,n,m,p0):
    P=[]
    dP=[]
    high=[0]*m
    low=[p0]*m
    alpha=(1-beta)*p0
    sigma_w=sigma*p0
    for j in range(n):
        P0=p0
        for i in range(m): 
            w=np.random.normal(0,1)
            P1=beta*P0+alpha+sigma_w*w
            dp=P1-P0
            P0=P1
            if P0>high[i]:
                high[i]=P0
            if P0<low[i]:
                low[i]=P0
            dP.append(dp)
        P.append(P0)
    price=pd.Series(P)
    dprice=pd.Series(dP)
    return price,dprice,high,low





price,dprice,high,low = ar1(0.9999,sigma,10000,250,1)


price,dprice,high,low = ar1(0.5,sigma,10000,250,1)
plt.figure(figsize=(8,4))
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
print("price std %2.5f"%price.std())





plt.show()

