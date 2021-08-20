# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 17:17:11 2021

@author: User
"""

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('EmpData.csv')


plt.scatter(df['Payment'],df['NoOfHours'])