#-*-coding:utf-8-*-
import pandas as pd
import string
import datetime
duqu=pd.read_csv(r'film_log3.csv',delimiter=';',names=['电影','上映日期','结束日期','公司','导演','演员','类型','票房','城市'])
print type(duqu)
duqu=duqu[(duqu['电影']=='《冲上云霄》')&((duqu['城市']=='武汉')|(duqu['城市']=='长沙'))]
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
print '上映天数为    '+`days`
sum=0.0
for i in duqu['票房']:
    i=string.atof(i.split('（万）')[-1])
    sum+=i
print '日平均票房为   '+`sum/days`