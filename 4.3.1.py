import pandas_datareader.data as web
import matplotlib.pyplot as plt

import numpy as np


start="1949/5/16"
end="2016/9/30"#適当に入れ替えてください。




price = web.DataReader("aapl", 'google',"1990/1/4",end)#yahooのサービスの停止により変更




dp=np.log(price.Close).diff()
vol=dp.std()*np.sqrt(250)
print(vol,len(price))



