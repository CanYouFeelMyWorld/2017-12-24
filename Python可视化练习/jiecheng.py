#-*-coding:utf-8 -*-
import numpy as np
a=np.arange(5)
print "a=",a
print "Clipped",a.clip(1,2)#修剪

a=np.arange(4)
print a
print "Compressed",a.compress(a>2)#压缩

#阶乘
b=np.arange(1,9)
print "b=",b
print "Factorial",b.prod()#数组元素的连乘积
print "Factorials",b.cumprod()#累计连乘

