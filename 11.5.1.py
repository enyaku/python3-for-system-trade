
import pandas_datareader.data as pdr
import numpy as np

import pandas_datareader.data as web




start='1971/12/1'
end='2016/8/31'
workpop = web.DataReader('LFWA64TTJPM647S',"fred",start,end).dropna()
gdp = web.DataReader('MKTGDPJPA646NWDB',"fred",start,end).dropna()
gdp=gdp.resample('A',loffset='-1d').last().dropna()
fx = web.DataReader('DEXJPUS',"fred",start,end).dropna()
fx=fx.resample('A',loffset='-1d').last().dropna()
workpop=workpop['1972':].resample('A',loffset='-1d').last().dropna()
gdpjpy=gdp.MKTGDPJPA646NWDB*fx.DEXJPUS
gdpjpy=np.log(gdpjpy).dropna()
workpop=np.log(workpop).dropna()

import statsmodels.api as sm
x=sm.add_constant(gdpjpy)
model=sm.OLS(gdpjpy,x)
results=model.fit()
print(results.summary())


import matplotlib.pyplot as plt


results.resid.hist(label='residual',color='seagreen')



import pandas as pd
lnn225 = np.log(pdr.DataReader("NIKKEI225", 'fred',start,end).dropna())
lnn225=lnn225.resample('A',loffset='-1d').last().dropna()
port=pd.concat([lnn225,x,gdpjpy],axis=1).dropna()
port.columns=["n225","const","workpop","gdpjpy"]
model=sm.OLS(port.n225,port.ix[0:,['const','workpop','gdpjpy']])
results=model.fit()
print(results.summary())







#バブル崩壊前
port_b=port[:'1990/1/1']
model_b=sm.OLS(port_b.n225,port_b.iloc[0:,1:])
results_b=model_b.fit()
print(results_b.summary())



