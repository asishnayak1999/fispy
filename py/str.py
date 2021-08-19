# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 11:49:12 2021

@author: User
"""

class A:
    def hello(self):
        print('hello')
        print('parent')
    def __str__(self):
        return 'My class ....'
    
obj = A()

print(obj)