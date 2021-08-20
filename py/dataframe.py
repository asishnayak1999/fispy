import pandas as pd

#d = [32,5,76,90,121,4]

#d = [['amit',21],['raj',23],['vivek',19],['ravi',31]]


d = {'rollno':[101,102,103,104],
     'name':['a','b','c','d'],
     'marks':[43,67,87,91]}

df = pd.DataFrame(d,index = ['rank1','rank2','rank3','rank4'])



print(df)
print(df['rollno'])
df['promote'] = df['marks']+10
print(df)