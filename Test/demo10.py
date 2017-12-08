#-*-coding:gb18030 -*-
import pandas as pd
import numpy as  np
import matplotlib as mpl
import string
import datetime
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
movie=pd.read_csv('ans020173.csv',delimiter=',',usecols=[1,4],header=0,encoding='gb18030',names=['电影','票房'])
moviename=movie['电影']
money=movie['票房']
name_list=[]
money_list=[]
for i in  moviename:
    name_list.append(i)
for i in  money:
    money_list.append(i)
x=range(len(name_list))
plt.xticks(x,name_list)
y=money_list
plt.plot(x,y,'yo-')
rect = plt.bar(x,y,align="center")
for x,y in zip(x,y):
    plt.text(x,y,'%.2f'%y)
# plt.yticks(y,money_list,rotation=45)
# plt.xticks(x, name_list, rotation=45)
# x=range(len(name_list))
plt.xlabel(u'电影名')
plt.ylabel(u'单位/万元')
plt.title(u'实时票房')
plt.margins(0.08)
plt.subplots_adjust(bottom=0.15)

plt.show()
