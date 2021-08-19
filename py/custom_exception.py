# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 13:41:34 2021

@author: User
"""





class MyExeption(Exception):
    def showmessage(self):
        print("My issue")
try:
    a = int(input("Number"))
    if a<10:
        raise MyExeption
    else:
        print('OK')

except MyExeption as ex:
    ex.showmessage()