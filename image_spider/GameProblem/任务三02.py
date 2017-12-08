#-*-coding:utf-8-*-
import pandas as pd
import string
import datetime
import matplotlib.pyplot as plt
list1=['《冲上云霄》','《一路惊喜》','《浪漫天降》']
list2=[]
for i in list1:
    duqu=pd.read_csv(r'film_log3.csv',delimiter=';',names=['电影','上映日期','结束日期','公司','导演','演员','类型','票房','城市'])
    print duqu

    duqu=duqu[(duqu['电影']==i)&((duqu['城市']=='武汉')|(duqu['城市']=='长沙'))]
    a=duqu['上映日期'].iloc[0].split('.')
    ay=string.atoi(a[0])
    am=string.atoi(a[1])
    ad=string.atoi(a[2])
    b=duqu['结束日期'].iloc[0].split('.')
    by=string.atoi(b[0])
    bm=string.atoi(b[1])
    bd=string.atoi(b[2])
    start=datetime.datetime(ay,am,ad)
    end=datetime.datetime(by,bm,bd)
    days=(end-start).days
    if days%7>0:
        zhou=days/7+1
    else:zhou=days/7
    sum=0.0
    for j in duqu['票房']:
        j=string.atof(j.split('（万）')[-1])
        sum+=j
    print i+'的周平均票房为   '+`sum/zhou`
    list2.append(sum/zhou)
plt.title(u'周平均票房')
plt.xlabel(u'电影')
plt.ylabel(u'票房(万)')
x=[0,1,2]
y=[list2[0],list2[1],list2[2]]
rect = plt.bar(x,y,align="center")
plt.xticks((0,1,2),(u'《冲上云霄》',u'《一路惊喜》',u'《浪漫天降》'))
plt.legend((rect),(u"图例"))
plt.show()
