# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 12:14:46 2021

@author: User
"""

import sys

try:
    x,op,y = int(sys.argv[1]),sys.argv[2],int(sys.argv[3])
    st = str(str(x) + op + str(y))
    result = eval(st)
    print(result)
except IndexError:
    print("No value provided")
except ValueError:
    print("Incorrect values provided")
except ZeroDivisionError:
    print("Can't device with zero")
    

