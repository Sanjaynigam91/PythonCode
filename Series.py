import pandas as pd

x=[1,2,3,4,5]

var=pd.Series(x,index=['a','b','c','d','e'],dtype='float')
print(var)

dic={"name":['Python','C#','Java','SQL'],"prop":[10,11,12,13],"rank":[1,3,2,4]}

result=pd.Series(dic)
print(result)

s1=[1,2,3,4,5]
d1=pd.Series(s1)
print(d1)

s2=[10,20,30,40,50]
d2=pd.Series(s2)
print(d2)

s=d1+d2
print(s)