
import pandas_datareader.data as web
import statsmodels.api as sm
import numpy as np

import matplotlib.pyplot as plt


end='2016/9/30'
n225 = web.DataReader("NIKKEI225", 'fred',"1949/5/16",end).dropna()
lnn225=np.log(n225.dropna())
lnn225.columns=['Close']
y=lnn225
x=range(len(lnn225))
x=sm.add_constant(x)
model=sm.OLS(y,x)
results=model.fit()

print(results.summary())






y=lnn225.loc['1986/12/1':'1993/10/31'].dropna()
x=range(len(y))
x=sm.add_constant(x)
model=sm.OLS(y,x)
results=model.fit()
print(results.summary())




y=lnn225.loc['1986/12/1':'1989/12/31'].dropna()
x=range(len(y))
x=sm.add_constant(x)
model=sm.OLS(y,x)
results=model.fit()
print(results.summary())


print("return ",np.exp(y.Close).pct_change().mean()*250)
print("volatility ",y.Close.diff().std()*np.sqrt(250))
print("std of residual",results.resid.std())
plt.plot(y,label='Close',color='darkgray')





y=lnn225.loc['1990/1/1':'1992/8/31'].dropna()
x=range(len(y))
x=sm.add_constant(x)
model=sm.OLS(y,x)
results=model.fit()
print(results.summary())


print("return ",np.exp(y.Close).pct_change().mean()*250)
print("volatility ",y.Close.diff().std()*np.sqrt(250))
print("std of residual",results.resid.std())
plt.plot(y,label='Close',color='seagreen')
results.fittedvalues.plot(label='prediction',style='--')
plt.legend()
plt.ylabel('log(n225 index)')

plt.show()
