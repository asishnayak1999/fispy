# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 12:56:07 2021

@author: User
"""
import pandas as pd

emp = {'empno':[1001,1002,1003,1004],
     'name':['Asish','Bharath','Aditya','Salman'],
     'Basepay':[12000,17000,21000,32000]}
df = pd.DataFrame(emp)

df['Hra'] = df['Basepay']+df['Basepay']*0.12

df['TotalPay'] = df['Hra'] + df['Basepay']

print(df)