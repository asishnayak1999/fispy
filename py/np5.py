# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 11:07:14 2021

@author: User
"""
import numpy as np
x = np.array([[12,43,65],
              [32,11,77],
              [12,90,65],
              [3,6,99]])

y = np.array([[2,4,6],
             [1,13,27],
             [90,45,19],
             [60,30,3]])


print(np.mod(x,y))

print(np.concatenate((x,y)))

print(np.concatenate((x,y),
                     axis=1))

print(np.split(x,2))

print(np.unique(x))

print(np.amin(x)) #min
print(np.amin(x,0)) #min col wise
print(np.amin(x,1)) #min row ise

print(np.amax(x)) #max
print(np.amax(x,0)) #max col wise
print(np.amax(x,1)) #max row wise

