# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 16:19:20 2021

@author: User
"""

import pymysql
#sstep1
d = pymysql.connect(host = 'localhost',user='root',
                password = 'Cloud@123$',
                db = 'fis')

#step2
cur = d.cursor()

sql = "select * from employee"

#step3
cur.execute(sql)
data = cur.fetchall()
for res in data:
    print("Emp no ",res[0])
    print("Name >>",res[1])
    print("City..",res[2])
    print("Salary..",res[3])
#print(data)
d.close()
