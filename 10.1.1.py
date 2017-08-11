

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

plt.show()

