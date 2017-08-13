
import pandas_datareader.data as web
start="1949/5/16"
end="2016/9/30"#適当に入れ替えてください。
N225 = web.DataReader("NIKKEI225", 'fred',start,end)
N225.head(1)

price = web.DataReader("NIKKEI225", 'fred',"1990/1/4",end)#yahooのサービスの停止により変更
price.head(1)

print(price.tail(1))


