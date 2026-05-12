import numpy as np
import pandas as pd
csv_file = pd.read_csv("C:\\Users\\Sanjay\\PycharmProjects\\PythonCode\\employee_dump_1000_records.csv",usecols=[0,1,3,4,5])
print(csv_file)

#get index
print(csv_file.index)

#get coulmns
print(csv_file.columns)

#use of Describe
print(csv_file.describe())

#use of head and tail
print(csv_file.head(20))
print(csv_file.tail(20))

#use of slicing
res=csv_file[:50]
print(res)
res1=csv_file[51:100]
print(res1)

#index as array
res2=csv_file.index.array
print(res2)

#Convert csv file into numpy array
res3=csv_file.to_numpy()
print(res3)

#Convert through numpy
res4=np.asarray(csv_file)
print(res4)

#Reverse csv data
res5=csv_file.sort_index(axis=0,ascending=False)
print(res5)

#Change the value of colum for particular row index
csv_file.loc[0,"Name"]="Prateek Kumar"
csv_file.loc[0,"Age"]=30
print(csv_file)

#get the particular row data
print(csv_file.loc[[3,4],["Name","Salary"]])
print(csv_file.loc[:,["Name","Salary"]])
print(csv_file.loc[[3,4],:])

#use of iloc to get the specific data
print(csv_file.iloc[0,3])

#Drop any column and row
print(csv_file.drop("Age", axis=1))
print(csv_file.drop(0,axis=0))