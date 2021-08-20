# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 13:39:13 2021

@author: User
"""

import matplotlib.pyplot as plt
import numpy as np

ct = ['india','Usa','UK']
pop = [1.35,1.80,1]

y = np.arange(len(ct))
plt.bar(y,pop)
plt.xticks(y,ct)
plt.title('Pop chart')
plt.show()