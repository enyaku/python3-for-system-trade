

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



def bernoulli(p,x,N,p0):
    s = (np.random.binomial(1, p, N)-0.5)*x
    P0=p0
    P=[]
    for i in range(N):
        P0=P0+s[i]
        P.append(P0)
    return P





N=10000
M=10000
Q=[]
for j in range(N):
    P=bernoulli(0.5,5,M,0)
    Q.append(P[M-1])
plt.figure(figsize=(8,5))
plt.figure.left=-0.1
plt.hist(Q,normed=True,histtype='stepfilled',color='lightyellow',bins=25)
plt.xlabel('$\sum_1^t B_t \cdot 5$')
plt.ylabel('probability density function')
price=pd.Series(Q)
dprice=price.diff()
print("mean %2.5f std %2.5f skew %2.5f kurt %2.5f"\
%(dprice.mean(),dprice.std(),dprice.skew(),dprice.kurt()))







plt.show()

