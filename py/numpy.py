# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 10:13:53 2021

@author: User
"""

import numpy as np

x = np.array([[12,43,65],
              [32,11,77],
              [12,90,65],
              [3,6,99]])

print(x[...,2]) #any row 2 column
print(x[2,...]) #2nd row clo 1 onwarnd
print(x[...,1:]) #any row 1 onwards

