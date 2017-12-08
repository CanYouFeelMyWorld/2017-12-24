#coding:utf-8
import pandas as pd
import matplotlib.pyplot as plt
duqu = pd.read_csv(r'text.csv',usecols=[2,5],header=0,names=['电影名称','实时票房'],encoding='utf-8')
list1 = duqu['电影名称']
list2 = duqu['实时票房']
dianying = []
piaofang = []
for i in list1:
    dianying.append(i)
for j in list2:
    piaofang.append(j)
X = range(len(dianying))
plt.xticks(X,dianying,rotation=-45)
plt.plot(X,piaofang,'o-')
for x,y in zip(X,piaofang):
    plt.text(x,y,'%.2f'%y)
plt.margins(0.08)
plt.subplots_adjust(bottom=0.15)
plt.xlabel(u"电影")
plt.ylabel(u"票房（万）")
plt.title(u"实时票房")
plt.show()

