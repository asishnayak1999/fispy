# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 11:18:46 2021

@author: User
"""

import numpy as np

x = np.array([[2,4,6],
             [1,13,27],
             [90,45,19],
             [60,30,3]])

print(x.T)

print(x.flatten(order='F'))
print(x.flatten())