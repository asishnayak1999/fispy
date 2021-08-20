# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 11:47:49 2021

@author: User
"""

import numpy as np

x = 'this is PYTHON'

print(np.char.lower(x))
print(np.char.upper(x))
print(np.char.title(x))
print(np.char.capitalize(x))
r = np.char.replace(x,'this','that')

print(r)

print(np.char.multiply('helllo',5))
print(np.char.array)