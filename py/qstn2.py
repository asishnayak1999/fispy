# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 13:34:46 2021

@author: User
"""
import pandas as pd
import matplotlib.pyplot as plt

emp = {'empno':[1001,1002,1003,1004],
     'name':['Asish','Bharath','Aditya','Salman'],
     'Basepay':[12000,17000,21000,32000]}

df = pd.DataFrame(emp)

print(df)

df['tax'] = df['Basepay']*0.3
print(df)
plt.bar(df['name'],df['tax'])