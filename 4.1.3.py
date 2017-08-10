import pandas_datareader.data as web
import matplotlib.pyplot as plt


start="1949/5/16"
end="2016/9/30"#適当に入れ替えてください。
N225 = web.DataReader("NIKKEI225", 'fred',start,end)

N225.head(1)
print(N225.head(1))

print("---------4.1.1------------")

N225.plot(color='darkblue')
plt.ylabel('N225 index')

#plt.show()
print("---------4.1.2------------")

price = web.DataReader("aapl", 'google',"1990/1/4",end)#yahooのサービスの停止により変更
price.head(1)

print(price.head(1))

print("---------4.1.3------------")


plt.show()

