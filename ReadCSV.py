import pandas as pd

#Read all data from CSV file
csv_file = pd.read_csv("C:\\Users\\Sanjay\\PycharmProjects\\PythonCode\\employee_dump_1000_records.csv")
print(csv_file)
print(type(csv_file))

#get the value at the position of 800
print(csv_file.iloc[[800]])

#read only top 10 rows
csv_file1 = pd.read_csv("C:\\Users\\Sanjay\\PycharmProjects\\PythonCode\\employee_dump_1000_records.csv",nrows=10)
print(csv_file1)
#Read only top 10 rows along with some specific column deta
csv_file2 = pd.read_csv("C:\\Users\\Sanjay\\PycharmProjects\\PythonCode\\employee_dump_1000_records.csv",nrows=10,usecols=[0,1,3,8])
print(csv_file2)

#Skip the column data
csv_file3 = pd.read_csv("C:\\Users\\Sanjay\\PycharmProjects\\PythonCode\\employee_dump_1000_records.csv",nrows=10,usecols=[0,1,3,8],
                        skiprows=[2])

#Change Index
print(csv_file3)
csv_file4 = pd.read_csv("C:\\Users\\Sanjay\\PycharmProjects\\PythonCode\\employee_dump_1000_records.csv",nrows=10,usecols=[0,1,3,8],
                       index_col="Name")
print(csv_file4)

#Change header
csv_file5 = pd.read_csv("C:\\Users\\Sanjay\\PycharmProjects\\PythonCode\\employee_dump_1000_records.csv",header=2)
print(csv_file5)

#Change the Header name
csv_file6 = pd.read_csv("C:\\Users\\Sanjay\\PycharmProjects\\PythonCode\\employee_dump_1000_records.csv",
                        names=["EmpID","EmpName","DepName","Age1","Salary1","Experience1","Status","City1","Score"],skiprows=[0],nrows=10,usecols=[0,1,3,4,8])
print(csv_file6)

#Change data type of Age and Salary Column
csv_file7 = pd.read_csv("C:\\Users\\Sanjay\\PycharmProjects\\PythonCode\\employee_dump_1000_records.csv",usecols=[0,1,3,4,8],
                        dtype={"Age": "float","Salary":"string"})
print(csv_file7)
