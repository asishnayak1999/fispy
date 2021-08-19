# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 14:32:01 2021

@author: User

"""
from datetime import datetime

datee = datetime.now()
if datee.day == 1:
    fn = input("enter file name to read")
    with open(fn) as obj1:
        with open("output.txt", "w") as obj2:
            for line in obj1:
                obj2.write(line)
    print("printing done")
else:
    print("Its not 1st of the month")