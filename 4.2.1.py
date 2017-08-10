import pandas_datareader.data as web
import matplotlib.pyplot as plt
import pandas as pd

start="1949/5/16"
end="2016/9/30"#適当に入れ替えてください。




price = web.DataReader("aapl", 'google',"1990/1/4",end)#yahooのサービスの停止により変更





fx = web.DataReader('DEXJPUS',"fred",start,end)
port=pd.concat([price.Close,fx],axis=1).dropna()
n=port.Close.pct_change().dropna()
f=port.DEXJPUS.pct_change().dropna()
f.rolling(window=20).corr(n).plot(color="yellow")
plt.ylabel('correlation')

plt.show()




