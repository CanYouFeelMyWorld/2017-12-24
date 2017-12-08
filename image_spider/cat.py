#-*- coding:utf-8 -*-
class Animal:
    def __init__(self ,color,heigh,weigh):
            self.color=color
            self.heigh=heigh
            self.weigh=weigh
    def __str__(self):
           msg= '颜色：%s'%self.color+'身高：%s'%self.heigh+'体重：%s'%self.weigh
           return msg
message=Animal("reb",180,70)
print message