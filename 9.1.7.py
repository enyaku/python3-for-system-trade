from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import pandas_datareader.data as web
import numpy as np
import matplotlib.pyplot as plt


plt.figure(figsize=(6,3))
ax=plt.subplot(1,1,1)

n225 = web.DataReader("NIKKEI225", 'fred',"1949/5/16").dropna()

rmax=float(n225.pct_change(10).max())
rmin=float(n225.pct_change(10).min())
rmax=int(rmax*100)/100.0
rmin=int(rmin*100)/100.0
nbins=30
dx=(rmax-rmin)/nbins
rc=int(rmin/2+rmax/2)/100.0
bins = np.arange(rmin, rmax, dx)
xyz=[]
k=0
start=1
end=250
for i in range(start,end):
    tmp=n225.pct_change(i).dropna()
    nn225=np.array(tmp)
    n, bin, rectangles = ax.hist(nn225, bins,normed=True)
    xyz.append([])
    for j in range(len(bins)-1):
        xyz[k].append(n[j])
    k+=1
xyz=np.array(xyz)
fig = plt.figure(figsize=(8,8))
ax = fig.gca(projection='3d')
Y = np.arange(0, len(n), 1)
X = np.arange(0, k-2, 1)
X, Y = np.meshgrid(X, Y)
Z = xyz[X,Y]#np.sqrt(X**2 + Y**2)
surf = ax.plot_surface(X, Y, Z, rstride=2, cstride=10, cmap=cm.Accent,
                       linewidth=0.5, antialiased=True)
plt.yticks([0,int(nbins/2),int(nbins)],[rmin,rc,rmax])
ax.set_xlabel='days'
ax.set_ylabel='ror'

plt.show()

