from operator import index

import pandas as pd

data=pd.DataFrame({"Even":[2,4,6,8,10],"Odd":[3,5,7,9,19]})
data1=pd.DataFrame({"Prime":[1,3,5,7,11],"Number":[12,13,14,15,16]})

print("**********Join two data frame *****************")
result=data.join(data1)
print(result)
print()

print("**********Join two data frame but 2nd Dataframe having less data ***************")
d1=pd.DataFrame({"Even":[2,4,6,8,10],"Odd":[3,5,7,9,19]})
d2=pd.DataFrame({"Prime":[1,3,5],"Number":[12,13,14]})
res=d1.join(d2)
print(res)
print()

print("**********Use of how(Left) parameter for join ***************")
res1=d1.join(d2,how="left")
print(res1)
print()

print("**********Use of how(Right) parameter for join ***************")
res2=d1.join(d2,how="right")
print(res2)
print()

print("**********Use of how(outer) parameter for join ***************")
res3=d1.join(d2,how="outer")
print(res3)
print()

print("**********Use of how(inner) parameter for join ***************")
res4=d1.join(d2,how="inner")
print(res4)
print()

print("**********Use of index parameter for join ***************")
d3=pd.DataFrame({"Even":[2,4,6,8,10],"Odd":[3,5,7,9,19]},index=["a","b","c","d","e"])
d4=pd.DataFrame({"Prime":[1,3,5],"Odd":[12,13,14]},index=["a","b","c"])
res5=d4.join(d3,how="outer",lsuffix="_Number",rsuffix="_Number")
print(res5)
print()

print("**********Use of Append function ***************")
d5=pd.DataFrame({"Even":[2,4,6,8,10],"Odd":[3,5,7,9,19]})
d6=pd.DataFrame({"Prime":[1,3,5],"Number":[12,13,14]})
res6=pd.concat([d5,d6],ignore_index=True,sort=False)
print(res6)
print()


