
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



#バブル崩壊前のグラフ
f,ax = plt.subplots()#２軸のグラフの準備
(port[:'1990/1/1'].gdpjpy-24).plot(label='gdp',linestyle="--",ax=ax)
port[:'1990/1/1'].n225.plot(label='n225',ax=ax)
ax2=ax.twinx()#２軸目をax2として設定
(port[:'1990/1/1'].workpop).plot(label='workpop',style='o',ax=ax2)
#書籍のグラフはworkpopから8.5引いてしまっているので、こちらが正しいグラフです。
results_b.fittedvalues.plot(label='fitted',style=':',ax=ax)
ax.set_ylabel('log Nikkei225 index')#1軸目にラベルを設定
ax2.set_ylabel('workshop')#2軸目にラベルを設定
ax.legend(loc='lower right')
ax2.legend(loc='upper left')





#バブル崩壊前：ヒストグラム
results_b.resid.hist(label='residual',color='lightyellow')
plt.xlabel('residual:gdp vs work population')
plt.ylabel('frequency')
plt.legend(loc='upper right')


#バブル崩壊後
port_a=port['1990/1/1':]
results_a=(sm.OLS(port_a.n225,port_a.iloc[0:,1:])).fit()
print(results_a.summary())


import pandas as pd
lnn225 = np.log(pdr.DataReader("NIKKEI225", 'fred',start,end).dropna())
lnn225=lnn225.resample('A',loffset='-1d').last().dropna()
lnfx=np.log(fx)
port1=pd.concat([lnn225,x,gdpjpy,lnfx],axis=1).dropna()
port1.columns=["n225","const","workpop","gdpjpy","fx"]
model1=sm.OLS(port1.n225,port1.iloc[0:,1:])
results1=model1.fit()
print(results1.summary())



#バブル崩壊後：要素にドル円の為替レートを追加
port1_a=port1['1990/1/1':]
results1_a=(sm.OLS(port1_a.n225,port1_a.iloc[0:,1:])).fit()
print(results1_a.summary())



##バブル崩壊後のグラフ：ドル円の為替レート
(port1['1990/1/1':].fx+5).plot(label='fx',linestyle="--")
port1['1990/1/1':].n225.plot(label='n225')
results1_a.fittedvalues.plot(label='fitted',style=':')
plt.ylabel('log Nikkei225 Index')
plt.legend(loc='lower left')



#バブル崩壊後：細分化
def report(port):
    results1_a=(sm.OLS(port1_a.n225,port1_a.iloc[0:,1:]))\
    .fit()
    print("R-squared: ",results1_a.rsquared," F-pvalue: ",results1_a.f_pvalue," AIC: "\
          ,results1_a.aic," BIC: ",results1_a.bic)
    print("pvalues: ")
    print(results1_a.pvalues)
    from statsmodels.compat import lzip
    import statsmodels.stats.api as sms
    test=sms.jarque_bera(results1_a.resid)
    print("jbpv: ",test[1])
port1_a=port1['1990/1/1':'2000/1/1']
report(port1_a)




#バブル崩壊後：細分化2
port1_a=port1.loc['2000/1/1':'2008/1/1']
report(port1_a)



#バブル崩壊後：細分化3
port1_a=port1.loc['2008/1/1':]
report(port1_a)



plt.show()
