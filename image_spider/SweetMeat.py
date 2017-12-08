# -*- coding:utf-8 -*-
class SweetMeat:
    def __init__(self):
        self.cookLevel=0
        self.cookedString='生的'
        self.condiments=[]

    def __str__(self):
            msg=self.cookedString+'牛肉'
            if len(self.cookedString)>0:
                msg=msg+"("
                for temp in self.condiments:
                    msg=msg+temp+","
                msg = msg.strip(", ")
                msg=msg+")"
            return msg
    def addcondiments(self,condiments):
        self.condiments.append(condiments)

    def cook(self,time):
        self.cookLevel+=time
        if self.cookLevel >=8:
            self.cookedString='吃碳吧兄弟'
        elif self.cookLevel>5:
            self.cookedString= '可以吃了'
        elif self.cookLevel>3:
            self.cookedString='还不能吃'
        else:
            self.cookedString
meat=SweetMeat()
print '开始烤肉了'
print ('开始时间：%d'%meat.cookLevel)
print ('烤肉情况:%s'%meat.cookedString)
print ('酱料:%s'%meat.condiments)
print '-'*30
print '3分钟后'
meat.cook(3)
meat.addcondiments("番茄酱")
print '烤肉情况:%s'%meat
print '4分钟后'
meat.cook(4)
print '烤肉情况:%s'%meat



