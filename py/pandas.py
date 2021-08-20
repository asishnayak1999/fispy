import pandas as pd

#s = pd.Series([32,54,1,90],index=['x','p','y','z'])

#print(s)

#print(s['x'])


st = {'roll':101,'name':'amit','city':'delhi','marks':91}

s = pd.Series(st,index=['city','name','roll','marks'])

print(s)


