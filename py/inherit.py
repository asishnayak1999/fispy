# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 11:38:38 2021

@author: User
"""

class A:
    def hello(self):
        print('hello')
        print('parent')
class B:
    def sum(self,a,b):
        print('sum',(a+b))

class C(A,B):
    def Hi(self):
        print("Hello c")
obj = C()

obj.hello()
obj.sum(12, 12)
obj.Hi()