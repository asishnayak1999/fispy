# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 10:54:59 2021

@author: User
"""

import numpy as np

x  = np.array([32,1,5,4,3,1,6,9])

y = x[2:7:2]

print(x[y])