# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 15:18:33 2021

@author: User
"""

f = open('empdetails.txt','r')

st = f.read(150)

print(st)

pos = f.tell()

print('position',pos)

pos = f.seek(0,0)

st = f.read(5)
print(st)

f.close()