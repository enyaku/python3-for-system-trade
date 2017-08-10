
import pandas_datareader.data as web
import statsmodels.api as sm
import numpy as np
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

