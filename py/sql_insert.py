# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 16:40:14 2021

@author: User
"""

import pymysql
try:
    #sstep1
    d = pymysql.connect(host = 'localhost',user='root',
                    password = 'Cloud@123$',
                    db = 'fis')
    
    
    cur = d.cursor()
    sql = "insert into employee values (104,'ravi','pune',10000);"
    
    cur.execute(sql)
    
    print('inserted')
    d.commit()
except Exception as ex:
    print(ex)
d.close()
