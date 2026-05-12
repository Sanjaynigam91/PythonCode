import pandas as pd

data={'Subject':['Hindi','Math','English','Science','Computer'],'Marks':[80,95,85,90,92],'Name':['Sanjay','Suraj','Ajay','Ramesh','Rahul']}
var =pd.DataFrame(data)
print(var)

print(type(var))
print(var.iloc[2])