
import pandas as pd
import pandas_datareader.data as web
import numpy as np
import matplotlib.pyplot as plt
n225 = web.DataReader("NIKKEI225", 'fred',"1949/5/16").dropna()
rn225=n225.pct_change().dropna()
plt.figure(figsize=(6,3))
ax=plt.subplot(1,1,1)
rn225.hist(bins=100,color='lightyellow',ax=ax)
plt.xlabel('$P_{t}/P_{t-1}-1$')
plt.ylabel('frequency')

plt.show()

