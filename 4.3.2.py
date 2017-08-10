import pandas_datareader.data as web
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd


start="1949/5/16"
end="2016/9/30"#適当に入れ替えてください。

price = web.DataReader("aapl", 'google',"1990/1/4",end)#yahooのサービスの停止により変更



dp=np.log(price.Close).diff()
vol=dp.std()*np.sqrt(250)
print(vol,len(price))


ma=pd.Series.rolling(price.Close,window=250).mean()
price.Close.plot(label='aapl Close',style='--')
ma.plot(label='250days ma')
plt.ylabel('aapl')
plt.legend()


(pd.Series.rolling(np.log(price.Close).diff().dropna(),window=25).std()*np.sqrt(250)).plot()
plt.ylabel('standrd deviation 250 days aapl')


plt.show()

