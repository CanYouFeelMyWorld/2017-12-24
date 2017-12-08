#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
x1=[1,2,3,4,5]
y1=[1,4,9,16,25]
x2=[1,2,4,6,8]
y2=[2,4,8,12,16]
plot1=pl.plot(x1,y1,'r')
# pl.plot(x1,y1,'oy')#散点图
plot2=pl.plot(x2,y2,'go')
# pl.plot(x2,y2,'o')#散点图
pl.title("Plot of y vs .x ")
pl.xlabel('x axis')
pl.ylabel('y axis')
pl.xlim(0.0,9.0)#x轴限度
pl.ylim(0.0,30.)#y轴限度
# pl.legend([plot1,plot2],('first','second'),loc='best',numpoints=1)
pl.legend([plot1,plot2])
pl.show()