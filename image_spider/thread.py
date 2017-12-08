#-*- coding:utf-8 -*-
import threading
from time import ctime,sleep
def music(func):
    for i in range(2):
        print  "i was listening to %s .%s"%(func,ctime())
        sleep(1)
def move(func):
    for i in range(2):
        print "i was at the %s! %s"%(func,ctime())
        sleep(5)
def dinner(funce):
    for i in range(2):
        print "i was eating dinner %s! %s"%(funce,ctime())
        sleep(7)
threads=[]
t1=threading.Thread(target=music,args=(u"LOL",))
threads.append(t1)
t2=threading.Thread(target=move,args=(u"Hello",))
threads.append(t2)
t3=threading.Thread(target=dinner,args=(u"apple",))
threads.append(t3)

if __name__=="__main__":
    # music(u'管你')
    # move(u'Hello')
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
    print "all over %s"%ctime()
