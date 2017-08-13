
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


#累積損益のグラフ表示
import matplotlib.pyplot as plt
session.on.cumsum().plot(label='$on$',linestyle=':')
session.s1.cumsum().plot(label='$s1$',style='.')
session.s12.cumsum().plot(label='$s12$',linestyle='-')
session.s2.cumsum().plot(label='$s2$',linestyle='--')
plt.legend(loc='upper left')
plt.ylabel('P&L')
#linestyleは線のタイプをしていする、4つのタイプがある。
#線(-）,点線（：）,破線（--）,破断線（-.）
#styleは線のスタイルを設定します。








plt.show()

