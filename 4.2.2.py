import pandas_datareader.data as web
import matplotlib.pyplot as plt
import pandas as pd

start="1949/5/16"
end="2016/9/30"#適当に入れ替えてください。

price = web.DataReader("aapl", 'google','1990/1/1',end)#yahooのサービスの停止により変更

price1=price.loc["1990/1/1":]#ixの停止によりlocに変更
price1.Close.plot(color='green')
price2=price["2015"].iloc[0:2]#ixの停止によりilocに変更
print(price2)
plt.ylabel('apple')



print(price.resample('M').first().tail())

print(price.resample('M').last().tail())


print(price.resample('M',loffset='1d').last().tail())



price.resample('A').Close.plot(color='magenta')
plt.ylabel('apple')


plt.show()




