
import pandas as pd
import pandas_datareader.data as web
import numpy as np
import matplotlib.pyplot as plt

n225 = web.DataReader("NIKKEI225", 'fred',"1949/5/16").dropna()
rn225=n225.pct_change().dropna()


plt.figure(figsize=(8,3))
ax=plt.subplot(1,2,1)
before=rn225.loc[:'1989/12/31']
before.hist(ax=ax,bins=100,color='lightyellow',normed=True)
plt.title('before bubble crashed')
plt.xlabel('$P_{t}/P_{t-1}-1$')
plt.ylabel('probability density function')
ax2=plt.subplot(1,2,2)
after=rn225.loc['1989/12/31':]
after.hist(ax=ax2,bins=100,color='lightyellow',normed=True)
plt.title('after bubble crashed')
plt.xlabel('$P_{t}/P_{t-1}-1$')
plt.ylabel('probability density function')


print("before crashed: mean %2.5f std %2.5f skew %2.5f kurt %2.5f"\
%(before.mean(),before.std(),before.skew(),before.kurt()))
print("after crashed: mean %2.5f std %2.5f skew %2.5f kurt %2.5f"\
%(after.mean(),after.std(),after.skew(),after.kurt()))


r250n225=n225.pct_change(250).dropna()

before250=r250n225.loc[:'1989/12/31']
print("before crashed: mean %2.5f std %2.5f skew %2.5f kurt %2.5f"\
%(before250.mean(),before250.std(),before250.skew(),before250.kurt()))
after250=r250n225.loc['1989/12/31':]
print("after crashed: mean %2.5f std %2.5f skew %2.5f kurt %2.5f"\
%(after250.mean(),after250.std(),after250.skew(),after250.kurt()))


plt.figure(figsize=(8,3))
ax3=plt.subplot(1,2,1)
before250.hist(ax=ax3,bins=100,color='lightgray',normed=True)
plt.title('before bubble crashed')
plt.xlabel('$P_{t}/P_{t-250}-1$')
plt.ylabel('probability density function')
ax4=plt.subplot(1,2,2)
after250.hist(ax=ax4,bins=100,color='lightgray',normed=True)
plt.title('after bubble crashed')
plt.xlabel('$P_{t}/P_{t-250}-1$')
plt.ylabel('probability density function')


plt.figure(figsize=(6,3.2))
ax5=plt.subplot(1,1,1)
before250.hist(ax=ax5,bins=100,normed=True,label='before',histtype="step")
after250.hist(ax=ax5,bins=100,normed=True,label='after',histtype="step",linestyle='--')
plt.xlabel('$P_{t}/P_{t-250}-1$')
plt.ylabel('probability density function')
plt.legend()


plt.show()

