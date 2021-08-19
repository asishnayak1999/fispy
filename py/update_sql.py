# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 16:46:12 2021

@author: User
"""

import pymysql
try:
    #sstep1
    d = pymysql.connect(host = 'localhost',user='root',
                    password = 'Cloud@123$',
                    db = 'fis')
    
    
    cur = d.cursor()
    sql = "update employee set salary=70000 where empno = 100;"
    
    cur.execute(sql)
    
    print('updated')
    d.commit()
    
except Exception as ex:
    print(ex)
d.close()