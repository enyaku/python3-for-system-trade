
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




session['s12c']=session.s12-2



#t統計量を利用した戦略
from scipy.stats import t

#カイ二乗統計量を利用した戦略
from scipy.stats import chi2

n=5


#トレンドの発生とボラティリティの安定性の判定
def long_stat(s,s0,t,t1):#統計的検定による買いポジションの判定
    stat=False
    if s<s0:#ボラティリティの安定性の判定
        if t>t1:#トレンドの有無の判定
            stat=True
    return stat

def create_port(session,session2,n):
    tt=(pd.Series.rolling(session,n).mean()/pd.Series.rolling(session,n).std()\
        *np.sqrt(n)).shift(1).dropna()
    ss=pd.Series.rolling(session,n).std().shift(1).dropna()
    #費用込みの損益、t値と標準偏差のデータベースの作成
    port=pd.concat([session2,ss,tt],axis=1).dropna()
    port.columns=['ror','s','t']
    return port
port=create_port(session.s12,session.s12c,n)

n=5
t0=t.ppf(0.4,n-1)#t統計量の算出
s0=chi2.ppf(0.7,n-1)*35/(n-1)#標準偏差の統計量の算出、35は真の値の推定値
port.ror[port.apply(lambda x:long_stat(x['s'],s0,x['t'],t0),axis=1)].cumsum()\
.plot(label='$s12$',linestyle='--')
session.s12c.cumsum().plot(label='$ror$',color='darkgreen')





session['s2c']=session.s2-2
port=create_port(session.s2,session.s2c,n)
plt.figure(figsize=(6,4))
n=5
t0=t.ppf(0.4,n-1)
s0=chi2.ppf(0.7,n-1)*96/(n-1)
port.ror[port.apply(lambda x:long_stat(x['s'],s0,x['t'],t0),axis=1)].cumsum().plot(label='$s2$',linestyle='--')
session.s2c.cumsum().plot(label='$ror$',color='darkgreen')
plt.ylabel('PL-p234-3')
plt.legend(loc='upper left')
print(s0,t0)





plt.show()

