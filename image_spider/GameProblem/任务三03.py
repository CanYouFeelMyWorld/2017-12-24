#-*-coding:utf-8-*-
import pandas as pd
import string
import datetime
import matplotlib.pyplot as plt
list1=['《冲上云霄》','《一路惊喜》','《浪漫天降》']
for i in list1:
    duqu=pd.read_csv(r'film_log3.csv',delimiter=';',names=['电影','上映日期','结束日期','公司','导演','演员','类型','票房','城市'])
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
    print i+'上映天数为    '+`days`
    sum=0.0
    for j in duqu['票房']:
        j=string.atof(j.split('（万）')[-1])
        sum+=j
    print i+'日平均票房为   '+`sum/days`
    list2=[]
    for t in range(0,days/7):
        list2.append(sum/days*7)
    rest=days%7*sum/days
    list2.append(rest)
    plt.title(u'折线图')
    plt.xlabel(u'周')
    plt.ylabel(u'票房（万）')
    plt.plot(list2)
plt.show()