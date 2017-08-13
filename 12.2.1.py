
#csvファイルからのデータの読み込み
import pandas as pd 
path = "/Users/yuanyue/Documents/GitHub/python3-for-system-trade/"
#fname="nikkei225fm_2_2015.csv"
fname="nkx_d_test.csv"

pathfname=path+fname
n225fm=pd.read_csv(pathfname,index_col=0,parse_dates=True)
#n225fm.head()

print(n225fm.head(1))

