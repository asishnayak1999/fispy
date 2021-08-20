import matplotlib.pyplot as plt
import pymysql

mydb = pymysql.connect(host='localhost',user='root',password='Cloud@123$',db='fis')

mycursor=mydb.cursor()

mycursor.execute("select * from employee;")
result = mycursor.fetchall()

ename = []
salary = []

for i in result:
    ename.append(i[1])
    salary.append(i[3])
    
plt.bar(ename,salary)

plt.legend()
plt.xlabel('name')
plt.ylabel('salary')
plt.show()
mydb.close()