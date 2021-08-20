import pandas as pd

#df = pd.read_csv('Emp.csv')
#df1 = pd.read_csv('EmpGrade.csv')
#df = pd.read_csv('salaries.csv')
#df = pd.read_csv('salaries.csv')

df = pd.read_csv('EmpData.csv')
#dt = df[(df['salary']>90000) & (df['discipline'] == 'B')]

#df['service'].fillna(df['service'].sum(),inplace= True)

#dt = df.dropna()

#df.insert(6,'test',df['service']+20)
#print(pd.merge(df,df1,on='EmpNo'))

#print(df.sort_values('salary',ascending=False))

#dc = df.groupby(['rank'])

#plt.hist()

dc = df.groupby(['city'])

total = dfg['Payment'].sum()

total.plot(kind =  'bar')

print(dc['salary'].sum())

 