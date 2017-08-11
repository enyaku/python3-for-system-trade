
import pandas as pd
import pandas_datareader.data as web
import numpy as np
import matplotlib.pyplot as plt

n225 = web.DataReader("NIKKEI225", 'fred',"1949/5/16").dropna()
rn225=n225.pct_change().dropna()




from scipy.stats import norm



fig=plt.figure(figsize=(6,3))
ax=plt.subplot(1,1,1)
r250n225=n225.pct_change(250).dropna()
x=np.linspace(float(r250n225.min()),float(r250n225.max()),100)
pdf=norm.pdf(x,r250n225.mean(),r250n225.std())
r250n225.hist(bins=100,color='lightyellow',normed=True,ax=ax)
plt.plot(x,pdf)
plt.xlabel('$P_{t}/P_{t-250}-1$')
plt.ylabel('probability density function')

print("mean %2.5f std %2.5f skew %2.5f kurt %2.5f"\
%(r250n225.mean(),r250n225.std(),r250n225.skew(),r250n225.kurt()))



plt.show()

