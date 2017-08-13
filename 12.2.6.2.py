
#csvファイルからのデータの読み込み
import pandas as pd 
path = "/Users/yuanyue/Documents/GitHub/python3-for-system-trade/"
#fname="nikkei225fm_2_2015.csv"

#fname="nkx_d_test4.csv"
fname="nkx_d_2017.csv"


pathfname=path+fname
n225fm=pd.read_csv(pathfname,index_col=0,parse_dates=True)
#n225fm.head()


#on,s1,s12,s2,onのデータベースの構築
from datetime import date, time,datetime
c0=int(n225fm.iloc[0].Close)
da0=n225fm[0:1].index.date
r=[];da=[];j=0;on=0;s1=0

cost=2
for i in range(1,len(n225fm)):
    d=n225fm[i:i+1].index
    t=n225fm[i:i+1].index.time
    o=int(n225fm.iloc[i].Open)
    c=n225fm.iloc[i].Close
    if t==time(9,0):
        s1=c-o
        on=o-c0
    if t==time(16,30):
        s2=c-o
        s12=o-c0
        da0=datetime(d.year[0],d.month[0],d.day[0])
        if da0==datetime(2016,7,15):
            s12=0
            s2=0
            c=c0
        da.append(da0)
        r.append([])
        r[j].append(on)
        r[j].append(s1)
        r[j].append(s12)
        r[j].append(s2)
        j+=1
    c0=c
session=pd.DataFrame(r,index=da)
session.columns=['on','s1','s12','s2']


#それぞれのセッション、セッション間の記述統計
print(session.s1.describe())
print(session.s12.describe())
print(session.s2.describe())
print(session.on.describe())

#各種統計量の算出、比較
import statsmodels.api as sm
import numpy as np
from statsmodels.compat import lzip
import statsmodels.stats.api as sms
print(sm.tsa.adfuller(session.s1,regression='nc')[1]) #[1]はp値の検定結果
print(sm.tsa.adfuller(session.s1,regression='c')[1]) #[1]はp値の検定結果
print(sm.tsa.adfuller(session.s1,regression='ct')[1]) #[1]はp値の検定結果
print(session.s1.mean()/session.s1.std()*np.sqrt(session.s1.count()))
estimator = ['JB', 'Chi-squared p-value', 'Skew', 'Kurtosis']
test = sms.jarque_bera(session.s1)
print('s1: ',lzip(estimator, test))



print(sm.tsa.adfuller(session.s12,regression='nc')[1]) #[1]はp値の検定結果
print(sm.tsa.adfuller(session.s12,regression='c')[1]) #[1]はp値の検定結果
print(sm.tsa.adfuller(session.s12,regression='ct')[1]) #[1]はp値の検定結果
print(session.s1.mean()/session.s12.std()*np.sqrt(session.s1.count()))
estimator = ['JB', 'Chi-squared p-value', 'Skew', 'Kurtosis']
test = sms.jarque_bera(session.s12)
print('s12: ',lzip(estimator, test))



print(sm.tsa.adfuller(session.s2,regression='nc')[1]) #[1]はp値の検定結果
print(sm.tsa.adfuller(session.s2,regression='c')[1]) #[1]はp値の検定結果
print(sm.tsa.adfuller(session.s2,regression='ct')[1]) #[1]はp値の検定結果
print(session.s2.mean()/session.s2.std()*np.sqrt(session.s2.count()))
estimator = ['JB', 'Chi-squared p-value', 'Skew', 'Kurtosis']
test = sms.jarque_bera(session.s2)
print('s2: ',lzip(estimator, test))





print(sm.tsa.adfuller(session.on,regression='nc')[1]) #[1]はp値の検定結果
print(sm.tsa.adfuller(session.on,regression='c')[1]) #[1]はp値の検定結果
print(sm.tsa.adfuller(session.on,regression='ct')[1]) #[1]はp値の検定結果
print(session.on.mean()/session.on.std()*np.sqrt(session.on.count()))
estimator = ['JB', 'Chi-squared p-value', 'Skew', 'Kurtosis']
test = sms.jarque_bera(session.on)
print('on: ',lzip(estimator, test))


import matplotlib.pyplot as plt


#s12におけるロングオンリー戦略のリターンの期間構造
plt.figure(figsize=(5,2.8))
high=[0]*151
low=[0]*151
ave=[0]*151
for i in range(151):
    high[i]=float(pd.Series.rolling(session.s12,i).sum().max())-2*i
    ave[i]=float(pd.Series.rolling(session.s12,i).sum().mean())-2*i
    low[i]=float(pd.Series.rolling(session.s12,i).sum().min())-2*i
plt.plot(high,label="high",linestyle=':')
plt.plot(ave,label='ave',color='darkred')
plt.plot(low,label='low',linestyle='--')
plt.legend(loc='upper left')
plt.xlabel('$t$')
plt.ylabel('PL')


plt.show()

