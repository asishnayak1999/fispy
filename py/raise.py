# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 13:31:10 2021

@author: User
"""

try:
    a = int(input("enter"))
    if a<10:
        raise Exception()
    else:
        print("okkkk")
except:
    print('issue is there')
finally:
    print("done donee")