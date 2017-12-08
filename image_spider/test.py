# -*- coding:utf-8 -*-
class base(object):
    def test(self):
        print 'base best'
class A(base):
    def test(self):
        print 'A test'
class B(base):
    def test(self):
        print 'B test'
class C(A,B):
    pass
obj_C=C()
obj_C.test()
print (C.__mro__)
